output_file=/home/pi/syncraftcore_kill_output.txt
echo "" > $output_file

# update IDEXConfig

cd /home/pi/printer_data/config
sudo git branch >> $output_file
sudo git stash >> $output_file
sudo git pull >> $output_file

if [ $? -neq 0 ]; then
	exit 1
fi

# TODO: Trocar para v1
sudo git checkout v1-homologacao >> $output_file
sudo git branch >> $output_file

# update SwierVision
cd /home/pi/SwierVision
sudo git stash >> $output_file
sudo git pull >> $output_file

if [ $? -neq 0 ]; then
	exit 1
fi

# TODO: Trocar para idex
sudo git checkout idex-dev >> $output_file

# replace rc.local with new one

cd /home/pi/printer_data/config
sudo rm -rf /etc/rc.local >> $output_file
sudo cp build/rc.local /etc >> $output_file

# remove SyncraftCore

cd /home/pi
sudo rm -rf SyncraftCore >> $output_file

sudo reboot