# rafaelSwi /*
# Defines what the machine will do when you start it.
# It calls the script inside SyncraftCore, which executes
# the others Python scripts inside the boot folder.

content='#!/bin/bash -e

syncraftcore_dir="/home/pi/SyncraftCore"
startup_dir="/home/pi/SyncraftCore/startup"
custom_startup_dir="/home/pi/SyncraftCore/custom_startup"

export DISPLAY=:0.0
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

exit 0
'

process='Modify RC.LOCAL.'
echo "[HELPER] START: $process."
echo -e "$content" | sudo tee /etc/rc.local
sudo chmod +x /etc/rc.local
echo "[HELPER] DONE: $process."