cd /home/pi

process="Update Syncraft Mainsail"
fresh_mainsail_dir=/home/pi/SyncraftCore/store/fresh/mainsail
machine_mainsail_dir=/home/pi/mainsail

echo "[HELPER] START: $process."
if [ -d "$machine_mainsail_dir" ]; then
    sudo rm -r $machine_mainsail_dir
fi
sudo cp -r $fresh_mainsail_dir /home/pi
echo "[HELPER] DONE: $process."