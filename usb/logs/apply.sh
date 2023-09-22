#!/bin/bash

name="[EXPORT LOGS TO USB]"

cd /home/pi/printer_data/gcodes/USB/*/

current_directory=$(pwd)
home_directory="$HOME"

if [ "$current_directory" = "$home_directory" ]; then
    echo "no USB folder detected"
    exit 0
fi

current_time=$(date +'%Y-%m-%d %H-%M')

folder_name="Syncraft Logs - $current_time"

if [ ! -d "$folder_name" ]; then
    sudo mkdir -p "$folder_name"
    echo "$name CREATED FOLDER: $folder_name"
fi

klippy_log_path="/home/pi/printer_data/logs/klippy.log"
moonraker_log_path="/home/pi/printer_data/logs/moonraker.log"
crowsnest_log_path="/home/pi/printer_data/logs/crowsnest.log"
klippy_usb_path="$folder_name/klipper.log"
moonraker_usb_path="$folder_name/moonraker.log"
crowsnest_usb_path="$folder_name/crowsnest.log"

if [ -f "$klippy_log_path" ]; then
    sudo cp "$klippy_log_path" "$klippy_usb_path"
    echo "$name OK: $klippy_log_path -> $klippy_usb_path"
else
    echo "$name NOT FOUND: $klippy_log_path"
fi

if [ -f "$moonraker_log_path" ]; then
    sudo cp "$moonraker_log_path" "$moonraker_usb_path"
    echo "$name OK: $moonraker_log_path -> $moonraker_usb_path"
else
    echo "$name NOT FOUND: $moonraker_log_path"
fi

if [ -f "$crowsnest_log_path" ]; then
    sudo cp "$crowsnest_log_path" "$crowsnest_usb_path"
    echo "$name OK: $crowsnest_log_path -> $crowsnest_usb_path"
else
    echo "$name NOT FOUND: $crowsnest_log_path"
fi