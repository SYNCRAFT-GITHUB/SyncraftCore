content="[Unit]
Description=Syncraft USB Mount Service

[Install]
WantedBy=graphical-session.target

[Service]
ExecStart=/usr/bin/udiskie --automount --no-config --notify --tray --appindicator
"

process='Create USB Service.'
echo "[HELPER] START: $process."
echo -e "$content" | sudo tee /etc/systemd/system/sxusb.service
echo "[HELPER] DONE: $process."

process='Create System Link in Gcodes Folder.'
echo "[HELPER] START: $process."
sudo ln -s /media/ /home/pi/printer_data/gcodes/
cd /home/pi/printer_data/gcodes
sudo mv media USB
mkdir .JOB
echo "[HELPER] DONE: $process."