import yaml
import os

core = os.path.join('/home', 'pi', 'SyncraftCore')
yaml_path = os.path.join(core, 'properties.yaml')

with open(yaml_path, 'r') as prop_file:
    dados_yaml = yaml.safe_load(prop_file)

dados_yaml['model'] = 'X2'

with open(yaml_path, 'w') as prop_file:
    yaml.dump(dados_yaml, prop_file)