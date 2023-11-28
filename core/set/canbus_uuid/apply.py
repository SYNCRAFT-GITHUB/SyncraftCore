import os
import yaml

CORE = os.path.join(os.path.dirname(__file__), '..', '..')
PROP = os.path.join('/Users/rafael/Desktop/wb/git/SyncraftCore', 'core', 'info.yaml')

print ('\n➤ Insert Canbus UUID:')
canbus_uuid = input("➤ ")

if canbus_uuid == '':
    exit()

with open(PROP, 'r') as yaml_file:
    data = yaml.safe_load(yaml_file)

data['canbus_uuid'] = canbus_uuid

with open(PROP, 'w') as yaml_file:
    yaml.dump(data, yaml_file, default_flow_style=False)