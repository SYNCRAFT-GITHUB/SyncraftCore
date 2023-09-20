cd /home/pi

process="Revert Klipper LED Effects"
stock_dir=/home/pi/SyncraftCore/stock/klipper-led_effect
softwares_dir=/home/pi/SyncraftCore/softwares/
machine_dir=/home/pi/klipper-led_effect

echo "[HELPER] START: $process."
if [ -d "$machine_dir" ]; then
    sudo rm -r $machine_dir
fi

sudo cp -r $stock_dir $softwares_dir
sudo cp -r $stock_dir /home/pi
cd "$machine_dir"
sudo -u pi bash install-led_effect.sh
echo "[HELPER] DONE: $process."