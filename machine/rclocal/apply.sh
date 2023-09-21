content='#!/bin/sh -e

startup_dir="/home/pi/SyncraftCore/startup"
custom_startup_dir="/home/pi/SyncraftCore/custom_startup"

RED="\033[0;31m"
GREEN="\033[0;32m"
YELLOW="\033[0;33m"
BLUE="\033[0;34m"
RESET="\033[0m"

if [ -d "$custom_startup_dir" ]; then
echo -e "${BLUE}[SyncraftCore Startup] ${YELLOW} Custom Startup Folder Detected.${RESET}"

    cd "$custom_startup_dir"

    for file in *.py; do
        if [ -f "$file" ]; then
            echo -e "${BLUE}[SyncraftCore Startup] ${YELLOW} (custom startup) EXECUTING: \"$file\""
            python3 "$file"
        fi
    done
elif [ -d "$startup_dir" ]; then
    echo -e "${BLUE}[SyncraftCore Startup] ${YELLOW} Startup Folder Detected.${RESET}"

    cd "$startup_dir"

    for file in *.py; do
        if [ -f "$file" ]; then
            echo -e "${BLUE}[SyncraftCore Startup] ${YELLOW} EXECUTING: \"$file\""
            python3 "$file"
        fi
    done
else
    echo -e "${BLUE}[SyncraftCore Startup] ${RED} Startup Folder not found!${RESET}"
fi

sleep 1 && sudo systemctl daemon-reload && service systemd-udevd --full-restart && sudo service sxusb start &

exit 0
'

process='Modify RC.LOCAL.'
echo "[HELPER] START: $process."
echo -e "$content" | sudo tee /etc/rc.local
sudo chmod +x /etc/rc.local
echo "[HELPER] DONE: $process."