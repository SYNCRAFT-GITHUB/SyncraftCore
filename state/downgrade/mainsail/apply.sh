cd /home/pi

process="Downgrade Syncraft Mainsail"
stock_mainsail_dir=/home/pi/SyncraftCore/store/stock/mainsail
fresh_mainsail_dir=/home/pi/SyncraftCore/store/fresh/mainsail
machine_mainsail_dir=/home/pi/mainsail

echo "[HELPER] START: $process."

if [ -d "$machine_mainsail_dir" ]; then
    sudo rm -r $machine_mainsail_dir
fi

if [ -d "$fresh_mainsail_dir" ]; then
    sudo rm -r $fresh_mainsail_dir
fi

sudo cp -r $stock_mainsail_dir $fresh_mainsail_dir
sudo cp -r $stock_mainsail_dir /home/pi

echo "[HELPER] DONE: $process."