cd /home/pi

process="Update Klipper LED Effects"
softwares_dir=/home/pi/SyncraftCore/softwares/klipper-led_effect
machine_dir=/home/pi/klipper-led_effect

echo "[HELPER] START: $process."
if [ -d "$machine_dir" ]; then
    sudo rm -r $machine_dir
fi

sudo cp -r $softwares_dir /home/pi
cd "$machine_dir"
sudo -u pi bash install-led_effect.sh
echo "[HELPER] DONE: $process."