#!/bin/sh

PID_FILE="/homebridge/scripts/crossfade_leo.pid"

if test -f "$PID_FILE"; then
    echo "true"
fi
