#!/bin/sh
pidfile=/homebridge/scripts/backdoor.pid
if [ -f "$pidfile" ] && kill -0 `cat $pidfile` 2>/dev/null; then
    echo still running
    exit 1
fi  

cd /homebridge/scripts && python3 garagedoor_reminder.py &
echo "Started $!"
echo $! >$pidfile
