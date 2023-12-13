content='#!/bin/bash -e

syncraftcore_dir="/home/pi/SyncraftCore"
startup_dir="/home/pi/SyncraftCore/startup"
custom_startup_dir="/home/pi/SyncraftCore/custom_startup"

if [ -d "$custom_startup_dir" ]; then

    source /home/pi/SyncraftCore/env/bin/activate
    cd "$syncraftcore_dir"
    sudo python3 -m custom_startup.script > /home/pi/bootlog.txt 2>&1

elif [ -d "$startup_dir" ]; then

    source /home/pi/SyncraftCore/env/bin/activate
    cd "$syncraftcore_dir"
    sudo python3 -m startup.script > /home/pi/bootlog.txt 2>&1

else
    echo -e "[SyncraftCore Startup] Startup Folder not found!"
fi

export DISPLAY=:0.0
if [ -f "/home/pi/SyncraftCore/intro/intro.py" ]; then
    cd "/home/pi/SyncraftCore/intro"
    sudo python3 intro.py
fi

exit 0
'

process='Modify RC.LOCAL.'
echo "[HELPER] START: $process."
echo -e "$content" | sudo tee /etc/rc.local
sudo chmod +x /etc/rc.local
echo "[HELPER] DONE: $process."