cd /home/pi

process="Revert Moonraker"
machine_dir=/home/pi/moonraker
stock_dir=/home/pi/SyncraftCore/stock/moonraker
softwares_dir=/home/pi/SyncraftCore/softwares
install_script=/home/pi/moonraker/scripts/install-moonraker.sh

echo "[HELPER] START: $process."
if [ -d "$machine_dir" ]; then
    sudo rm -r $machine_dir
fi

sudo cp -r $stock_dir $softwares_dir
sudo cp -r $stock_dir /home/pi

if [ -e "$install_script" ]; then
    sudo -u pi bash $install_script
fi

echo "[HELPER] DONE: $process."