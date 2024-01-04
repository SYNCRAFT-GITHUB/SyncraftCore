# rafaelSwi /*
# Install the necessary python packages on the machine
# without using a python environment

echo "[HELPER] Install python3-pip"

sudo apt-get install python3-pip

echo "[HELPER] Install req using pip"

pip3 install -r /home/pi/SyncraftCore/core/requirements.txt