import os
import yaml
from dirs import DIR

# rafaelSwi /*
# Applies an ID to the SyncraftCore "info" file,
# not directly to the .cfg file that klipper reads.

def set_main_canbus_uuid():

    print ('\n➤ Insert Canbus UUID (main mcu):')
    canbus_uuid = input("➤ ")

    if canbus_uuid == '':
        return None

    with open(DIR.CORE.INFO, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)

    data['main_canbus_uuid'] = canbus_uuid

    with open(DIR.CORE.INFO, 'w') as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=False)