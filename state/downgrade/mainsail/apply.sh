cd /home/pi

process="Downgrade Syncraft Mainsail"
stock_mainsail_dir=/home/pi/SyncraftCore/store/stock/mainsail
machine_mainsail_dir=/home/pi/mainsail

echo "[HELPER] START: $process."
if [ -d "$machine_mainsail_dir" ]; then
    sudo rm -r $machine_mainsail_dir
fi
sudo cp -r $stock_mainsail_dir /home/pi
echo "[HELPER] DONE: $process."