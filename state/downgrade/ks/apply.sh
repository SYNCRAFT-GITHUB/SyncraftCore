cd /home/pi

process="Downgrade Syncraft KlipperScreen"
stock_ks_dir=/home/pi/SyncraftCore/store/stock/KlipperScreenIDEX
fresh_ks_dir=/home/pi/SyncraftCore/store/fresh/KlipperScreenIDEX
machine_ks_dir=/home/pi/KlipperScreen

echo "[HELPER] START: $process."

if [ -d "$machine_ks_dir" ]; then
    sudo rm -r $machine_ks_dir
fi

if [ -d "$fresh_ks_dir" ]; then
    sudo rm -r $fresh_ks_dir
fi

sudo cp -r $stock_ks_dir $fresh_ks_dir
sudo cp -r $stock_ks_dir $machine_ks_dir
echo "[HELPER] DONE: $process."