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
        final_model += 'X1'
    if 'X2' in model.upper():
        final_model += 'X2'
    else:
        print ('unknown model')
        dados_yaml['model'] = 'X1'
        return None
    
    if (type == 'stable'):
        pass
    if (type == 'beta'):
        final_model += '-BETA'
    if (type == 'dev'):
        final_model += '-DEV'
    
    return final_model

args = parser.parse_args()

with open(yaml_path, 'r') as prop_file:
    dados_yaml = yaml.safe_load(prop_file)

dados_yaml['model'] = create_model_prop(args.model, args.type)

with open(yaml_path, 'w') as prop_file:
    yaml.dump(dados_yaml, prop_file)