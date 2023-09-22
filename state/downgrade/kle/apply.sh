cd /home/pi

process="Downgrade Klipper LED Effects"
stock_kle_dir=/home/pi/SyncraftCore/store/stock/klipper-led_effect
machine_kle_dir=/home/pi/klipper-led_effect

echo "[HELPER] START: $process."
if [ -d "$machine_kle_dir" ]; then
    sudo rm -r $machine_kle_dir
fi

sudo cp -r $stock_kle_dir /home/pi
cd "$machine_kle_dir"
sudo -u pi bash install-led_effect.sh
echo "[HELPER] DONE: $process."