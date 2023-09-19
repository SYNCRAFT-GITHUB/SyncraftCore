cd ~

process="Update Syncraft X1 KlipperScreen"
softwares_dir=~/SyncraftCore/softwares/KlipperScreen
machine_dir=~/KlipperScreen

echo "[HELPER] START: $process."
if [ -d "$machine_dir" ]; then
    sudo rm -r $machine_dir
fi
sudo cp -r $softwares_dir ~/
echo "[HELPER] DONE: $process."