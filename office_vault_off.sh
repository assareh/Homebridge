#!/bin/sh

# create a variable to represent the filename
PID_FILE="/homebridge/scripts/office_vault.pid"

# read in the process from the file
pid=`cat $PID_FILE`

# log
echo "Going to kill $pid and clean up $PID_FILE"

# kill
kill $pid

# clean up
rm -rf $PID_FILE

# turn off the light
python3 /homebridge/scripts/office_off.py
