#!/bin/bash

# rafaelSwi /*
# This method is considered outdated and not safe for systems with SyncraftCore.
# If its use is necessary, there's a flaw somewere that must be fixed.

cd /home/pi

moonraker_dir=/home/pi/moonraker
script_dir=/home/pi/moonraker/scripts/install-moonraker.sh

process='Re-Install Moonraker'

echo "[HELPER] START: $process."
if [ -d "$moonraker_dir" ]; then
    sudo rm -r $moonraker_dir
fi

git clone --quiet https://github.com/SYNCRAFT-GITHUB/moonraker.git

if [ -e "$script_dir" ]; then
    bash $script_dir
fi

echo "[HELPER] DONE: $process."

sudo reboot