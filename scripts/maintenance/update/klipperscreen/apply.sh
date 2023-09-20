cd /home/pi

process="Update Syncraft X1 KlipperScreen"
softwares_dir=/home/pi/SyncraftCore/softwares/KlipperScreen
machine_dir=/home/pi/KlipperScreen

echo "[HELPER] START: $process."
if [ -d "$machine_dir" ]; then
    sudo rm -r $machine_dir
fi
sudo cp -r $softwares_dir /home/pi
echo "[HELPER] DONE: $process."