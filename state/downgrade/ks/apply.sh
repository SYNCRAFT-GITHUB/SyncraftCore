cd /home/pi

process="Downgrade Syncraft SwierVision"
stock_sv_dir=/home/pi/SyncraftCore/store/stock/SwierVision
fresh_sv_dir=/home/pi/SyncraftCore/store/fresh/SwierVision
machine_sv_dir=/home/pi/SwierVision

echo "[HELPER] START: $process."

if [ -d "$machine_sv_dir" ]; then
    sudo rm -r $machine_sv_dir
fi

if [ -d "$fresh_sv_dir" ]; then
    sudo rm -r $fresh_sv_dir
fi

sudo cp -r $stock_sv_dir $fresh_sv_dir
sudo cp -r $stock_sv_dir $machine_sv_dir
echo "[HELPER] DONE: $process."