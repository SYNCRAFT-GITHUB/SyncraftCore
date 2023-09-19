process='Install Udiskie'
echo "[HELPER] START: $process."
sudo apt-get install -qqy udiskie
echo "[HELPER] DONE: $process."

process='Install LightDM'
echo "[HELPER] START: $process."
sudo apt-get install -qqy lightdm
echo "[HELPER] DONE: $process."

process='Install VLC Player'
echo "[HELPER] START: $process."
sudo apt-get install -qqy vlc
echo "[HELPER] DONE: $process."

process='Install MPlayer'
echo "[HELPER] START: $process."
sudo apt-get install -qqy mplayer
echo "[HELPER] DONE: $process."