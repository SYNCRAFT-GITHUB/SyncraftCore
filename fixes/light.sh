#!/bin/bash

# rafaelSwi /*
# This method is considered outdated and not safe for systems with SyncraftCore.
# If its use is necessary, there's a flaw somewere that must be fixed.

cd /home/pi

process='Install Klipper LED Effect'
echo "[HELPER] START: $process."

if [ -e "/home/pi/klipper-led_effect" ]; then
    sudo rm -r klipper-led_effect
fi

git clone --quiet https://github.com/julianschill/klipper-led_effect.git
bash /home/pi/klipper-led_effect/install-led_effect.sh

echo "[HELPER] DONE: $process."

sudo reboot