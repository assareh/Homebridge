FROM oznu/homebridge:4.0.0

# install pip
RUN /usr/bin/python -m ensurepip

# install requests
RUN /usr/bin/python -m pip install requests hvac