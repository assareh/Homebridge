#!/bin/sh

# create a variable to represent the filename
PID_FILE="/homebridge/scripts/office_terraform.pid"

if test -f "$PID_FILE"; then
    echo "true"
fi
