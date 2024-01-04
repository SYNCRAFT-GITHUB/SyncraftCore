# rafaelSwi /*
# Creates the service necessary to use USB Devices.
# Also creates a link in the klipper gcodes folder to the
# directory that the USB will appear within the system.

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