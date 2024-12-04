import os
import configparser
import json

config = configparser.ConfigParser()
config.read("/home/pi/printer_data/config/printer.cfg")

if "mcu" in config:
	mcu_canbus_uuid = config["mcu"]["canbus_uuid"]

if "mcu rp2040" in config:
	mcu_rp2040_canbus_uuid = config["mcu rp2040"]["canbus_uuid"]

canbus_uuids_json = {
	"mcu": mcu_canbus_uuid,
	"mcu rp2040": mcu_rp2040_canbus_uuid
}

with open("/home/pi/printer_data/config/canbus_uuids.json", "w") as canbus_uuids_json_file:
	json.dump(canbus_uuids_json, canbus_uuids_json_file)

os.system("sh /home/pi/SyncraftCore/startup/startup.sh")