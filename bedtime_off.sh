#!/bin/sh

# create a variable to represent the filename
PID_FILE="/homebridge/scripts/bedtime.pid"

# read in the process from the file
pid=`cat $PID_FILE`

# log
echo "Going to kill $pid and clean up $PID_FILE"

# kill
kill $pid

# clean up
rm -rf $PID_FILE
