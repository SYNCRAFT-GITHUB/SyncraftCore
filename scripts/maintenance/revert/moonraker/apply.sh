cd ~

process="Revert Moonraker"
machine_dir=~/moonraker
stock_dir=~/SyncraftCore/stock/moonraker
softwares_dir=~/SyncraftCore/softwares
install_script=~/moonraker/scripts/install-moonraker.sh

echo "[HELPER] START: $process."
if [ -d "$machine_dir" ]; then
    sudo rm -r $machine_dir
fi

sudo cp -r $stock_dir $softwares_dir
sudo cp -r $stock_dir ~/

if [ -e "$install_script" ]; then
    bash $install_script
fi

echo "[HELPER] DONE: $process."