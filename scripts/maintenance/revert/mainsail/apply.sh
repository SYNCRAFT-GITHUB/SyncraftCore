cd ~

process="Revert Syncraft Mainsail"
stock_dir=~/SyncraftCore/stock/mainsail
softwares_dir=~/SyncraftCore/softwares/
machine_dir=~/mainsail

echo "[HELPER] START: $process."
if [ -d "$machine_dir" ]; then
    sudo rm -r $machine_dir
fi

sudo cp -r $stock_dir $softwares_dir
sudo cp -r $stock_dir ~/
echo "[HELPER] DONE: $process."