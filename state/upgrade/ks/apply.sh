cd /home/pi

process="Update Syncraft KlipperScreen"
fresh_ks_dir=/home/pi/SyncraftCore/store/fresh/KlipperScreenIDEX
machine_ks_dir=/home/pi/KlipperScreen

echo "[HELPER] START: $process."
if [ -d "$machine_ks_dir" ]; then
    sudo rm -r $machine_ks_dir
fi
sudo cp -r $fresh_ks_dir $machine_ks_dir
echo "[HELPER] DONE: $process."