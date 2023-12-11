#!/bin/bash

name="[EXPORT CUSTOM MATERIALS TO USB]"

cd /home/pi/printer_data/gcodes/USB/*/

current_directory=$(pwd)
home_directory="$HOME"

if [ "$current_directory" = "$home_directory" ]; then
    echo "no USB folder detected"
    exit 0
fi

current_time=$(date +'%Y-%m-%d %H-%M')

folder_name="Syncraft Materials - $current_time"

if [ ! -d "$folder_name" ]; then
    sudo mkdir -p "$folder_name"
    echo "$name CREATED FOLDER: $folder_name"
fi

custom_materials_path="/home/pi/SyncraftCore/materials/custom.json"
custom_materials_usb_path="$folder_name/materials.json"

if [ -f "$custom_materials_path" ]; then
    sudo cp "$custom_materials_path" "$custom_materials_usb_path"
    echo "$name OK: $custom_materials_path -> $custom_materials_usb_path"
else
    echo "$name NOT FOUND: $custom_materials_path"
fi