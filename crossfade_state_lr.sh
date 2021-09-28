#!/bin/sh

PID_FILE="/homebridge/scripts/crossfade_lr.pid"

if test -f "$PID_FILE"; then
    echo "true"
fi
