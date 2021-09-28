#!/bin/bash
python /homebridge/scripts/bedtime_fade.py &
echo $! >/homebridge/scripts/bedtime.pid
echo "Started $!"
