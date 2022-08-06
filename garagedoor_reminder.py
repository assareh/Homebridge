import asyncio
import hvac
import logging
import os

from aiohttp import ClientSession

from pymyq import login
from pymyq.account import MyQAccount
from pymyq.errors import MyQError, RequestError
from pymyq.garagedoor import STATE_CLOSED, STATE_OPEN

from twilio.rest import Client


_LOGGER = logging.getLogger()

EMAIL = os.environ['MYQ_EMAIL']
PASSWORD = os.environ['MYQ_PASSWORD']
ISSUE_COMMANDS = False
# LOGLEVEL = logging.DEBUG
LOGLEVEL = logging.WARNING

FROM_PHONE = os.environ['TWILIO_FROM_PHONE']
TO_PHONE_1 = os.environ['TWILIO_TO_PHONE_1']
TO_PHONE_2 = os.environ['TWILIO_TO_PHONE_2']
ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']


def send_message():
    # Sign in to Twilio
    print(f"Signing in to Twilio to send a message...")
    SMS_CLIENT = Client(ACCOUNT_SID, AUTH_TOKEN)

    ## Begin Twilio ------------------------------------------------------------------------ ##
    SMS_CLIENT.messages.create(body="Please close the garage door.",
                            to=TO_PHONE_1,
                            from_=FROM_PHONE)

    SMS_CLIENT.messages.create(body="Please close the garage door.",
                            to=TO_PHONE_2,
                            from_=FROM_PHONE)
    ## End Twilio ------------------------------------------------------------------------ ##


def print_info(number: int, device):
    """Print the device information

    Args:
        number (int): [description]
        device ([type]): [description]
    """
    print(f"      Device {number + 1}: {device.name}")
    print(f"      Device Online: {device.online}")
    print(f"      Device ID: {device.device_id}")
    print(
        f"      Parent Device ID: {device.parent_device_id}",
    )
    print(f"      Device Family: {device.device_family}")
    print(
        f"      Device Platform: {device.device_platform}",
    )
    print(f"      Device Type: {device.device_type}")
    print(f"      Firmware Version: {device.firmware_version}")
    print(f"      Open Allowed: {device.open_allowed}")
    print(f"      Close Allowed: {device.close_allowed}")
    print(f"      Current State: {device.state}")
    print("      ---------")

    if device.state == 'open':
        send_message()
    elif device.state == 'opening':
        send_message()


async def print_garagedoors(account: MyQAccount):  # noqa: C901
    """Print garage door information and open/close if requested

    Args:
        account (MyQAccount): Account for which to retrieve garage doors
    """
    print(f"  GarageDoors: {len(account.covers)}")
    print("  ---------------")
    if len(account.covers) != 0:
        for idx, device in enumerate(account.covers.values()):
            print_info(number=idx, device=device)

            if ISSUE_COMMANDS:
                try:
                    open_task = None
                    opened = closed = False
                    if device.open_allowed:
                        if device.state == STATE_OPEN:
                            print(f"Garage door {device.name} is already open")
                        else:
                            print(f"Opening garage door {device.name}")
                            try:
                                open_task = await device.open(wait_for_state=False)
                            except MyQError as err:
                                _LOGGER.error(
                                    "Error when trying to open %s: %s",
                                    device.name,
                                    str(err),
                                )
                            print(f"Garage door {device.name} is {device.state}")

                    else:
                        print(f"Opening of garage door {device.name} is not allowed.")

                    # We're not waiting for opening to be completed before we do call to close.
                    # The API will wait automatically for the open to complete before then
                    # processing the command to close.

                    if device.close_allowed:
                        if device.state == STATE_CLOSED:
                            print(f"Garage door {device.name} is already closed")
                        else:
                            if open_task is None:
                                print(f"Closing garage door {device.name}")
                            else:
                                print(
                                    f"Already requesting closing garage door {device.name}"
                                )

                            try:
                                closed = await device.close(wait_for_state=True)
                            except MyQError as err:
                                _LOGGER.error(
                                    "Error when trying to close %s: %s",
                                    device.name,
                                    str(err),
                                )

                    if open_task is not None and not isinstance(open_task, bool):
                        opened = await open_task

                    if opened and closed:
                        print(
                            f"Garage door {device.name} was opened and then closed again."
                        )
                    elif opened:
                        print(f"Garage door {device.name} was opened but not closed.")
                    elif closed:
                        print(f"Garage door {device.name} was closed but not opened.")
                    else:
                        print(f"Garage door {device.name} was not opened nor closed.")

                except RequestError as err:
                    _LOGGER.error(err)
        print("  ------------------------------")


async def main() -> None:
    """Create the aiohttp session and run the example."""
    logging.basicConfig(level=LOGLEVEL)
    async with ClientSession() as websession:
        try:
            # Create an API object:
            # print(f"{EMAIL} {PASSWORD}")
            api = await login(EMAIL, PASSWORD, websession)

            for account in api.accounts.values():
                print(f"Account ID: {account.id}")
                print(f"Account Name: {account.name}")

                # Get all devices listed with this account – note that you can use
                # api.covers to only examine covers or api.lamps for only lamps.
                await print_garagedoors(account=account)


        except MyQError as err:
            _LOGGER.error("There was an error: %s", err)


asyncio.get_event_loop().run_until_complete(main())

