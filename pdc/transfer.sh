# rafaelSwi /*
# Everything in this directory will be copied and pasted into the klipper config folder.
# (This includes this exact script, but that's okay.)

overwrite_dir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
destination_dir="/home/pi/printer_data/config/"

for file in "$overwrite_dir"/*; do
    if [ -f "$file" ]; then
    sudo cp $file $destination_dir
    echo "[*] $file -> $destination_dir"
    fi
done