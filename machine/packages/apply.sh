# rafaelSwi: Install the necessary Linux system packages on the machine

install_package() {
    local name="$1"
    echo "[HELPER] START: $name."
    sudo apt-get install -qqy $name
echo "[HELPER] DONE: $name."
}

install_package "udiskie"
install_package "vlc"
install_package "mplayer"
install_package "python3-venv"
install_package "python3-git"
install_package "python3-pip"
install_package "python3-can"