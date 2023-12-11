cd /home/pi

name="[MATERIALS IMPORT SCRIPT]"

cd /home/pi/printer_data/gcodes/USB/*/

current_directory=$(pwd)
home_directory="$HOME"

if [ "$current_directory" = "$home_directory" ]; then
    echo "no USB folder detected"
    exit 0
fi

materials_usb_path="SYNCRAFT/materials/materials.json"
custom_materials_core_path="/home/pi/SyncraftCore/materials/custom.json"

if [ -f "$materials_usb_path" ]; then
    echo "$materials_usb_path dont exist."
    exit 0
fi

sudo cp $materials_usb_path $custom_materials_core_path
sudo chown pi:1000 $custom_materials_core_path
 