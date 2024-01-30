# rafaelSwi /*
# Creates some essential Canbus interface/communication files.
# Useful information:
# Link 1: https://github.com/Esoterical/voron_canbus
# Link 2: https://github.com/Esoterical/voron_canbus/tree/main/mainboard_flashing

content="allow-hotplug can0
iface can0 can static
  bitrate 1000000
  up ip link set can0 txqueuelen 1024
"

process='Create can0 file.'
echo "[HELPER] START: $process."
echo -e "$content" | sudo tee /etc/network/interfaces.d/can0
echo "[HELPER] DONE: $process."

####################################################################

content="[Match]
Type=can

[Link]
TransmitQueueLength=1024
"

process='Create can .link file.'
echo "[HELPER] START: $process."
echo -e "$content" | sudo tee /etc/systemd/network/10-can.link
echo "[HELPER] DONE: $process."

####################################################################

content="[Match]
Name=can*

[CAN]
BitRate=1M
"

process='Create can bitrate file.'
echo "[HELPER] START: $process."
echo -e "$content" | sudo tee /etc/systemd/network/25-can.network
echo "[HELPER] DONE: $process."