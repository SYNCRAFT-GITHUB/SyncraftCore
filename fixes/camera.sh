#!/bin/bash

# rafaelSwi /*
# This method is considered outdated and not safe for systems with SyncraftCore.
# If its use is necessary, there's a flaw somewere that must be fixed.

cd /home/pi

process='Install Crowsnest'
echo "[HELPER] START: $process."

if [ -e "/home/pi/crowsnest" ]; then
    sudo rm -r /home/pi/crowsnest
fi

git clone -b master https://github.com/mainsail-crew/crowsnest.git
cd /home/pi/crowsnest
sudo make install

echo "[HELPER] DONE: $process."

sudo reboot