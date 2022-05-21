FROM oznu/homebridge:latest

# install pip
RUN /usr/bin/python -m ensurepip

# install requests
RUN /usr/bin/python -m pip install requests hvac