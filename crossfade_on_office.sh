#!/bin/sh
python /homebridge/scripts/crossfade.py 3 &
echo $! >/homebridge/scripts/crossfade_office.pid
echo "Started $!"
