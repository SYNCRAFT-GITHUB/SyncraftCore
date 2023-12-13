content='#!/bin/bash -e

syncraftcore_dir="/home/pi/SyncraftCore"
startup_dir="/home/pi/SyncraftCore/startup"
custom_startup_dir="/home/pi/SyncraftCore/custom_startup"

if [ -d "$custom_startup_dir" ]; then

    source /home/pi/SyncraftCore/env/bin/activate
    cd "$syncraftcore_dir"
    sudo python3 -m custom_startup.script | sudo tee /home/pi/bootlog.txt > /dev/null

elif [ -d "$startup_dir" ]; then

    source /home/pi/SyncraftCore/env/bin/activate
    cd "$syncraftcore_dir"
    sudo python3 -m startup.script | sudo tee /home/pi/bootlog.txt > /dev/null

else
    echo -e "[SyncraftCore Startup] Startup Folder not found!"
fi

export DISPLAY=:0.0
if [ -f "/home/pi/SyncraftCore/intro/intro.py" ]; then

    source /home/pi/SyncraftCore/env/bin/activate
    cd "$syncraftcore_dir"
    sudo python3 -m intro.intro | sudo tee /home/pi/bootlog.txt > /dev/null
fi

exit 0
'

process='Modify RC.LOCAL.'
echo "[HELPER] START: $process."
echo -e "$content" | sudo tee /etc/rc.local
sudo chmod +x /etc/rc.local
echo "[HELPER] DONE: $process."