#!/bin/sh
python3 /homebridge/scripts/crossfade.py 3 &
echo $! >/homebridge/scripts/crossfade_office.pid
echo "Started $!"
