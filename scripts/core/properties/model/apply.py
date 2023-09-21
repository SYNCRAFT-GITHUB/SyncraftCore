import os
import argparse
import git
import yaml

core = os.path.join('/home', 'pi', 'SyncraftCore')
yaml_path = os.path.join(core, 'properties.yaml')

parser = argparse.ArgumentParser(description="Update SyncraftCore Software's Branch")
parser.add_argument("--model", required=True, help="Syncraft MODEL")
parser.add_argument("--type", required=True, help="stable/beta/dev")

def create_model_prop(model: str, type: str) -> str:

    final_model: str = ''

    if 'X1' in model.upper():
        final_model += 'syncraftx1'
    elif 'X2' in model.upper():
        final_model += 'syncraftx2'
    else:
        print ('unknown model')
        return None
    
    if (type == 'stable'):
        pass
    if (type == 'beta'):
        final_model += '-beta'
    if (type == 'dev'):
        final_model += '-dev'

    return final_model

args = parser.parse_args()

with open(yaml_path, 'r') as prop_file:
    dados_yaml = yaml.safe_load(prop_file)

dados_yaml['model'] = create_model_prop(args.model, args.type).lower()

with open(yaml_path, 'w') as prop_file:
    yaml.dump(dados_yaml, prop_file)