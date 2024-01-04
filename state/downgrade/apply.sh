#!/bin/bash

# rafaelSwi /*
# Reset all software to factory defaults stored on the machine,
# restore the USB settings, and then restart the machine.
# It's probably one of the only scripts that reboots at the end.

dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

for folder in "$dir"/*; do
    if [ -d "$folder" ]; then
        if [ -f "$folder/apply.sh" ]; then
            echo "RUNNING: $folder"
            (cd "$folder" && sudo bash apply.sh)
        fi
    fi
done

content="[Unit]
Description=Syncraft USB Mount Service

[Install]
WantedBy=graphical-session.target

[Service]
ExecStart=/usr/bin/udiskie --automount --no-config --notify --tray --appindicator
"

gcodes_dir=/home/pi/printer_data/gcodes

process='Create USB Service.'
echo "[HELPER] START: $process."
echo -e "$content" | sudo tee /etc/systemd/system/sxusb.service
echo "[HELPER] DONE: $process."

process='Create System Link in Gcodes Folder.'
echo "[HELPER] START: $process."

if [ -d "$gcodes_dir/" ]; then
    sudo rm -rf $gcodes_dir/*
else
    sudo mkdir -p $gcodes_dir
fi
sudo ln -s /media/ $gcodes_dir
cd $gcodes_dir
sudo mv media USB
mkdir .JOB

echo "[HELPER] DONE: $process."

sudo reboot