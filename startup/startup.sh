# reclone IDEXConfig
cd /home/pi/printer_data/config
cp printer.cfg /home/pi/tmp-printer.cfg
cp canbus_uuids.json /home/pi/tmp-canbus_uuids.json
cp variables.cfg /home/pi/tmp-variables.cfg
cp SwierVision.conf /home/pi/tmp-SwierVision.conf
cd /home/pi/printer_data
git clone -b v1 https://github.com/SYNCRAFT-GITHUB/IDEXConfig.git
if [ $? -neq 0 ]; then
	exit 1
fi
sudo chown -R pi IDEXConfig
rm -rf config
mv IDEXConfig config
mv /home/pi/tmp-printer.cfg config/printer.cfg
mv /home/pi/tmp-canbus_uuids.json config/canbus_uuids.json
mv /home/pi/tmp-variables.cfg config/variables.cfg 
mv /home/pi/tmp-SwierVision.conf config/SwierVision.conf

# reclone SwierVision
cd /home/pi
git clone -b idex https://github.com/SYNCRAFT-GITHUB/SwierVision.git SwierVisionNew
if [ $? -neq 0 ]; then
	exit 1
fi
rm -rf SwierVision
mv SwierVisionNew SwierVision
sudo chown -R pi SwierVision

# remove SyncraftCore
cd /home/pi
rm -rf SyncraftCore

# replace new rc.local
cd /home/pi/printer_data/config
rm -rf /etc/rc.local
cp build/rc.local /etc
sudo chmod +x /etc/rc.local

reboot