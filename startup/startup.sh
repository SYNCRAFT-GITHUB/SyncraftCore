# update IDEXConfig

cd /home/pi
cd printer_data/config
sudo git stash >> /home/pi/idexconfig_output.txt
sudo git pull >> /home/pi/idexconfig_output.txt

if [ $? -neq 0 ]; then
	exit 1
fi

# TODO: Trocar para v1
sudo git checkout v1-homologacao >> /home/pi/idexconfig_output.txt

# update SwierVision
cd /home/pi
cd SwierVision
sudo git stash >> /home/pi/idexconfig_output.txt
sudo git pull >> /home/pi/idexconfig_output.txt

if [ $? -neq 0 ]; then
	exit 1
fi

# TODO: Trocar para idex
sudo git checkout idex-dev >> /home/pi/idexconfig_output.txt

# replace rc.local with new one

cd /home/pi
cd printer_data/config
sudo rm -rf /etc/rc.local >> /home/pi/idexconfig_output.txt
sudo cp build/rc.local /etc >> /home/pi/idexconfig_output.txt

# remove SyncraftCore

cd /home/pi
sudo rm -rf SyncraftCore >> /home/pi/idexconfig_output.txt

sudo reboot