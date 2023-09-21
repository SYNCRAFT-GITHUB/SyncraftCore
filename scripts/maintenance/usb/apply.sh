name="[UPDATE USING USB]"

core_dir=/home/pi/SyncraftCore
softwares_dir=$core_dir/softwares

usb_dir=/home/pi/printer_data/gcodes/USB/*
syncraft_dir=$usb_dir/SYNCRAFT
content_dir=$syncraft_dir/content

kle_dir=$content_dir/klipper-led_effect
pdc_dir=$content_dir/printerdataconfig
moonraker_dir=$content_dir/moonraker
mainsail_dir=$content_dir/mainsail
ks_dir=$content_dir/KlipperScreen

copy_content() {

    local copy="$1"
    local software_name="$2"

    echo "$name Copying Content: $software"

    if [ -d "$copy" ]; then
        if [ -d "$softwares_dir/$software_name" ]; then
            sudo rm -r $softwares_dir/$software_name
        fi
        sudo cp -r $copy $softwares_dir
    fi

    echo "$name Done: $software"

}

copy_content $kle_dir "klipper-led_effect"
copy_content $pdc_dir "printerdataconfig"
copy_content $moonraker_dir "moonraker"
copy_content $mainsail_dir "mainsail"
copy_content $ks_dir "KlipperScreen"

sudo bash /home/pi/SyncraftCore/scripts/maintenance/update/apply.sh
