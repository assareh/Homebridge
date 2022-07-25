#!/bin/sh
allColors=("terraform" "vault" "consul" "nomad" "boundary" "waypoint" "vagrant" "packer")

for color in ${allColors[@]}; do
echo $color
tee office_${color}_on.sh <<EOO
#!/bin/sh
python3 /homebridge/scripts/office_$color.py &
echo $! >/homebridge/scripts/office_$color.pid
echo "Started \$!"
EOO
tee office_${color}_off.sh <<EOF
#!/bin/sh

# create a variable to represent the filename
PID_FILE="/homebridge/scripts/office_$color.pid"

# read in the process from the file
pid=\`cat \$PID_FILE\`

# log
echo "Going to kill \$pid and clean up \$PID_FILE"

# kill
kill \$pid

# clean up
rm -rf \$PID_FILE

# turn off the light
python3 /homebridge/scripts/office_off.py
EOF
tee office_${color}_state.sh <<EOS
#!/bin/sh

# create a variable to represent the filename
PID_FILE="/homebridge/scripts/office_$color.pid"

if test -f "\$PID_FILE"; then
    echo "true"
fi
EOS
tee -a config.json <<EOC
        {
            "accessory": "Script2",
            "name": "Office Lamp $color",
            "on": "/homebridge/scripts/office_${color}_on.sh",
            "off": "/homebridge/scripts/office_${color}_off.sh",
            "state": "/homebridge/scripts/office_${color}_state.sh",
            "on_value": "true"
        },
EOC
done
