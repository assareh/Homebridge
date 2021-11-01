#!/bin/sh

PID_FILE="/homebridge/scripts/office.pid"

if test -f "$PID_FILE"; then
    echo "true"
fi
