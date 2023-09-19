cd ~

process="Update Syncraft Mainsail"
softwares_dir=~/SyncraftCore/softwares/mainsail
machine_dir=~/mainsail

echo "[HELPER] START: $process."
if [ -d "$machine_dir" ]; then
    sudo rm -r $machine_dir
fi
sudo cp -r $softwares_dir ~/
echo "[HELPER] DONE: $process."