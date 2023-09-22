install_package() {
    local name="$1"  # First argument
    echo "[HELPER] START: $name."
    sudo apt-get install -qqy $name
echo "[HELPER] DONE: $name."
}

install_package "udiskie"
install_package "lightdm"
install_package "vlc"
install_package "mplayer"