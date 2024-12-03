# update IDEXConfig

cd /home/pi
cd printer_data/config
git checkout v1-homologacao
git pull

if [ $? -neq 0 ]; then
	exit 1
fi

# replace rc.local with new one

sudo rm -rf /etc/rc.local
sudo cp config/build/rc.local /etc

# remove SyncraftCore

cd /home/pi
rm -rf SyncraftCore

sudo reboot