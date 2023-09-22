cd /home/pi

process="Update Syncraft X1 KlipperScreen"
fresh_ks_dir=/home/pi/SyncraftCore/store/fresh/KlipperScreen
machine_ks_dir=/home/pi/KlipperScreen

echo "[HELPER] START: $process."
if [ -d "$machine_ks_dir" ]; then
    sudo rm -r $machine_ks_dir
fi
sudo cp -r $fresh_ks_dir /home/pi
echo "[HELPER] DONE: $process."