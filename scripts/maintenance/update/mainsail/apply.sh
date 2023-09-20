cd /home/pi

process="Update Syncraft Mainsail"
softwares_dir=/home/pi/SyncraftCore/softwares/mainsail
machine_dir=/home/pi/mainsail

echo "[HELPER] START: $process."
if [ -d "$machine_dir" ]; then
    sudo rm -r $machine_dir
fi
sudo cp -r $softwares_dir /home/pi
echo "[HELPER] DONE: $process."