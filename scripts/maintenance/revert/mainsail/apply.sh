cd /home/pi

process="Revert Syncraft Mainsail"
stock_dir=/home/pi/SyncraftCore/stock/mainsail
softwares_dir=/home/pi/SyncraftCore/softwares/
machine_dir=/home/pi/mainsail

echo "[HELPER] START: $process."
if [ -d "$machine_dir" ]; then
    sudo rm -r $machine_dir
fi

sudo cp -r $stock_dir $softwares_dir
sudo cp -r $stock_dir /home/pi
echo "[HELPER] DONE: $process."