#!/bin/sh
python3 /homebridge/scripts/crossfade.py 2 &
echo $! >/homebridge/scripts/crossfade_lr.pid
echo "Started $!"
