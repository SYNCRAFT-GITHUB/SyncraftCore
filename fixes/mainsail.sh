#!/bin/bash

cd /home/pi

process='Apply Syncraft Mainsail'
echo "[HELPER] START: $process."

mainsail_dir=/home/pi/mainsail
stock_dir=/home/pi/SyncraftCore/store/stock

if [ -d "$mainsail_dir" ]; then
    sudo rm -r $mainsail_dir
fi
mkdir $mainsail_dir
cd $mainsail_dir
wget -q https://github.com/SYNCRAFT-GITHUB/mainsail/releases/latest/download/mainsail.zip
unzip -q mainsail.zip

if [ -d "$stock_dir/mainsail" ]; then
    sudo rm -r $stock_dir/mainsail
fi
mkdir $stock_dir/mainsail
cd $stock_dir/mainsail
wget -q https://github.com/SYNCRAFT-GITHUB/mainsail/releases/latest/download/mainsail.zip
unzip -q mainsail.zip

echo "[HELPER] DONE: $process."

sudo reboot