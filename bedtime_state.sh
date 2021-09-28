#!/bin/sh

PID_FILE="/homebridge/scripts/bedtime.pid"

if test -f "$PID_FILE"; then
    echo "true"
fi
