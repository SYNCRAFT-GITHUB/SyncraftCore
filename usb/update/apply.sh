#################
# KLIPPERSCREEN #
#################

cd /home/pi

name="[USB UPDATE SCRIPT]"

process="$name Update Syncraft KlipperScreen"
softwares_dir=/home/pi/printer_data/gcodes/USB/*/SYNCRAFT/content/KlipperScreenIDEX
fresh_dir=/home/pi/SyncraftCore/state/fresh/KlipperScreenIDEX

echo "[HELPER] START: $process."
if [ -d "$fresh_dir" ]; then
    sudo rm -r $fresh_dir
fi
sudo cp -r $softwares_dir /home/pi
sudo chown -R pi:1000 $fresh_dir
echo "[HELPER] DONE: $process."


############
# MAINSAIL #
############

cd /home/pi

process="$name Update Syncraft Mainsail"
softwares_dir=/home/pi/printer_data/gcodes/USB/*/SYNCRAFT/content/mainsail
fresh_dir=/home/pi/SyncraftCore/state/fresh/mainsail

echo "[HELPER] START: $process."
if [ -d "$fresh_dir" ]; then
    sudo rm -r $fresh_dir
fi
sudo cp -r $softwares_dir /home/pi
sudo chown -R pi:1000 $fresh_dir
echo "[HELPER] DONE: $process."


#############
# MOONRAKER #
#############

cd /home/pi

process="$name Update Moonraker"
fresh_dir=/home/pi/SyncraftCore/state/fresh/moonraker
softwares_dir=/home/pi/printer_data/gcodes/USB/*/SYNCRAFT/content/moonraker
install_script=/home/pi/SyncraftCore/state/fresh/moonraker/scripts/install-moonraker.sh

echo "[HELPER] START: $process."
if [ -d "$fresh_dir" ]; then
    sudo rm -r $fresh_dir
fi
sudo cp -r $softwares_dir /home/pi

if [ -e "$install_script" ]; then
    sudo -u pi bash $install_script
fi

sudo chown -R pi:1000 $fresh_dir

echo "[HELPER] DONE: $process."


##############
# IDEXConfig #
##############

cd /home/pi

process="$name Update IDEXConfig"
fresh_dir=/home/pi/SyncraftCore/state/fresh/IDEXConfig
softwares_dir=/home/pi/printer_data/gcodes/USB/*/SYNCRAFT/content/config

echo "[HELPER] START: $process."
if [ -d "$fresh_dir" ]; then
    sudo rm -r $fresh_dir
fi

sudo cp -r $softwares_dir /home/pi/printer_data/

sudo chown -R pi:1000 $fresh_dir

echo "[HELPER] DONE: $process."

echo "[HELPER] ALL DONE!"