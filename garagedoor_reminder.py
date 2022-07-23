import os
import hvac
from twilio.rest import Client


FROM_PHONE = os.environ['TWILIO_FROM_PHONE']
TO_PHONES = os.environ['TWILIO_TO_PHONES']
ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

# Sign in to Twilio
SMS_CLIENT = Client(ACCOUNT_SID, AUTH_TOKEN)

## Begin Twilio ------------------------------------------------------------------------ ##
for TO_PHONE in TO_PHONES:
    SMS_CLIENT.messages.create(body="Please close the garage door.",
                                to=TO_PHONE,
                                from_=FROM_PHONE)
## End Twilio ------------------------------------------------------------------------ ##
