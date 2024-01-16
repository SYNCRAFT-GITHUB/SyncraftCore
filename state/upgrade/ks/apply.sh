cd /home/pi

process="Update Syncraft SwierVision"
fresh_sv_dir=/home/pi/SyncraftCore/store/fresh/SwierVision
machine_sv_dir=/home/pi/SwierVision

echo "[HELPER] START: $process."
if [ -d "$machine_sv_dir" ]; then
    sudo rm -r $machine_sv_dir
fi
sudo cp -r $fresh_sv_dir $machine_sv_dir
echo "[HELPER] DONE: $process."