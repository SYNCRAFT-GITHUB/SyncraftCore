cd ~

process="Revert Klipper LED Effects"
stock_dir=~/SyncraftCore/stock/klipper-led_effect
softwares_dir=~/SyncraftCore/softwares/
machine_dir=~/klipper-led_effect

echo "[HELPER] START: $process."
if [ -d "$machine_dir" ]; then
    sudo rm -r $machine_dir
fi

sudo cp -r $stock_dir $softwares_dir
sudo cp -r $stock_dir ~/
cd "$machine_dir"
./install-led_effect.sh
echo "[HELPER] DONE: $process."