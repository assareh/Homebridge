#!/bin/sh
python3 /homebridge/scripts/crossfade.py 4 &
echo $! >/homebridge/scripts/crossfade_leo.pid
echo "Started $!"
