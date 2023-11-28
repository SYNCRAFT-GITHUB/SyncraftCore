import os
import yaml

PROP = os.path.join('/home', 'pi', 'SyncraftCore', 'core', 'info.yaml')

print ('\n➤ Insert Canbus UUID:')
canbus_uuid = input("➤ ")

if canbus_uuid == '':
    exit()

with open(PROP, 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)

data['canbus_uuid'] = canbus_uuid

with open(PROP, 'w') as yaml_file:
    yaml.dump(data, yaml_file, default_flow_style=False)