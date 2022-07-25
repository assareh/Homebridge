#!/bin/sh
python3 /homebridge/scripts/bedtime_fade.py &
echo $! >/homebridge/scripts/bedtime.pid
echo "Started $!"
