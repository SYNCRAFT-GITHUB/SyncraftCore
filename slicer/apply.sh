#!/bin/bash

script_directory="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cd ~/printer_data/gcodes/USB/*/

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

sudo cp -r "$script_directory/mac" "$folder_name"
sudo cp -r "$script_directory/windows" "$folder_name"


if [ $? -eq 0 ]; then
    echo "Directory copied successfully to \"$folder_name\"."
else
    echo "Failed to copy directory"
fi