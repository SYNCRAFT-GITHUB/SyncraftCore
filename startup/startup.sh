# update IDEXConfig

cd /home/pi
cd printer_data/config
git stash
git pull

if [ $? -neq 0 ]; then
	exit 1
fi

# TODO: Trocar para v1
git checkout v1-homologacao

# update SwierVision
cd /home/pi
cd SwierVision
git stash
git pull

if [ $? -neq 0 ]; then
	exit 1
fi

# TODO: Trocar para idex
git checkout idex-dev

# replace rc.local with new one

cd /home/pi
cd printer_data/config
sudo rm -rf /etc/rc.local
sudo cp build/rc.local /etc

# remove SyncraftCore

cd /home/pi
rm -rf SyncraftCore

sudo reboot