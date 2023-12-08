cd /home/pi

process="Downgrade Syncraft KlipperScreen"
stock_ks_dir=/home/pi/SyncraftCore/store/stock/KlipperScreenIDEX
machine_ks_dir=/home/pi/KlipperScreen

echo "[HELPER] START: $process."
if [ -d "$machine_ks_dir" ]; then
    sudo rm -r $machine_ks_dir
fi
sudo cp -r $stock_ks_dir /home/pi
echo "[HELPER] DONE: $process."