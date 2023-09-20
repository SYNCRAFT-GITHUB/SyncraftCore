cd /home/pi

process="Update Moonraker"
machine_dir=/home/pi/moonraker
softwares_dir=/home/pi/SyncraftCore/softwares/moonraker
install_script=/home/pi/moonraker/scripts/install-moonraker.sh

echo "[HELPER] START: $process."
if [ -d "$machine_dir" ]; then
    sudo rm -r $machine_dir
fi
sudo cp -r $softwares_dir /home/pi

if [ -e "$install_script" ]; then
    sudo -u pi bash $install_script
fi

echo "[HELPER] DONE: $process."