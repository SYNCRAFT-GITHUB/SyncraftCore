content='#!/bin/sh -e

startup_dir="/home/pi/SyncraftCore/startup"
custom_startup_dir="/home/pi/SyncraftCore/custom_startup"

if [ -d "$custom_startup_dir" ]; then

    cd "$custom_startup_dir"

    for file in *.py; do
        if [ -f "$file" ]; then
            python3 "$file" > /home/pi/start_log.txt 2>&1
        fi
    done
elif [ -d "$startup_dir" ]; then

    cd "$startup_dir"

    for file in *.py; do
        if [ -f "$file" ]; then
            python3 "$file" > /home/pi/start_log.txt 2>&1
        fi
    done
else
    echo -e "[SyncraftCore Startup] Startup Folder not found!"
fi

export DISPLAY=:0.0
if [ -f "/home/pi/SyncraftCore/intro/intro.py" ]; then
    cd "/home/pi/SyncraftCore/intro"
    sudo python3 intro.py
fi

sleep 1 && sudo systemctl daemon-reload && service systemd-udevd --full-restart && sudo service sxusb start &

exit 0
'

process='Modify RC.LOCAL.'
echo "[HELPER] START: $process."
echo -e "$content" | sudo tee /etc/rc.local
sudo chmod +x /etc/rc.local
echo "[HELPER] DONE: $process."