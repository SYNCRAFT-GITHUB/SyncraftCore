# update IDEXConfig

cd /home/pi
cd printer_data/config
git pull

if [ $? -neq 0 ]; then
	exit 1
fi

git stash
# TODO: Trocar para v1
git checkout v1-homologacao

# replace rc.local with new one

sudo rm -rf /etc/rc.local
sudo cp build/rc.local /etc

# remove SyncraftCore

cd /home/pi
rm -rf SyncraftCore

sudo reboot