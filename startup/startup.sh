# update IDEXConfig

cd /home/pi
cd printer_data/config
sudo git stash
sudo git pull

if [ $? -neq 0 ]; then
	exit 1
fi

# TODO: Trocar para v1
sudo git checkout v1-homologacao

# update SwierVision
cd /home/pi
cd SwierVision
sudo git stash
sudo git pull

if [ $? -neq 0 ]; then
	exit 1
fi

# TODO: Trocar para idex
sudo git checkout idex-dev

# replace rc.local with new one

cd /home/pi
cd printer_data/config
sudo rm -rf /etc/rc.local
sudo cp build/rc.local /etc

# remove SyncraftCore

cd /home/pi
sudo rm -rf SyncraftCore

sudo reboot