cd ~

process="Update Klipper LED Effects"
softwares_dir=~/SyncraftCore/softwares/klipper-led_effect
machine_dir=~/klipper-led_effect

echo "[HELPER] START: $process."
if [ -d "$machine_dir" ]; then
    sudo rm -r $machine_dir
fi

sudo cp -r $softwares_dir ~/
cd "$machine_dir"
./install-led_effect.sh
echo "[HELPER] DONE: $process."