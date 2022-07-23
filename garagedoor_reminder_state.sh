#!/bin/sh

PID_FILE="/homebridge/scripts/backdoor.pid"

if test -f "$PID_FILE"; then
    echo "true"
fi
