#!/bin/bash

script_directory="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd /home/pi/printer_data/gcodes/USB/*/

current_time=$(date +'%Y-%m-%d %H-%M')
folder_name="Syncraft Installers - $current_time"

current_directory=$(pwd)
home_directory="$HOME"

if [ "$current_directory" = "$home_directory" ]; then
    echo "directory error"
    exit 0
fi

if [ ! -d "$folder_name" ]; then
    sudo mkdir -p "$folder_name"
fi

sudo cp "$script_directory/installer-mac.zip" "$folder_name"
sudo cp "$script_directory/installer-windows.zip" "$folder_name"


if [ $? -eq 0 ]; then
    echo "Copied successfully to \"$folder_name\"."
else
    echo "Failed to copy..."
fi