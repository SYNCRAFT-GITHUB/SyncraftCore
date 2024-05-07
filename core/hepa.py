from dirs import DIR
import argparse
import yaml
import datetime
import os

def set_hepa_start(action: str):

    if not os.path.exists(DIR.CORE.INFO):
        print(f'Prop file does not exists.')
        return

    with open(DIR.CORE.INFO, 'r') as arquivo:

        prop = yaml.safe_load(arquivo)

        if action == 'start':
            prop['last-hepa-replacement'] = datetime.date.today().strftime('%Y-%m-%d')
            print(f'last-hepa-replacement: {prop["last-hepa-replacement"]}')
            with open(DIR.CORE.INFO, 'w') as arquivo:
                yaml.dump(prop, arquivo)
            return

        if "hepa-count" in prop:
            if action == "+":
                prop['hepa-count'] = int(prop.get('hepa-count')) + 1
            elif action == "-":
                if int(prop.get('hepa-count')) > 0:
                    prop['hepa-count'] = int(prop.get('hepa-count')) - 1
        else:
            if action == "+":
                prop['hepa-count'] = 1
            elif action == "-":
                prop['hepa-count'] = 0

    with open(DIR.CORE.INFO, 'w') as arquivo:
        yaml.dump(prop, arquivo)
        return

parser = argparse.ArgumentParser(description='Manage HEPA filter information')
parser.add_argument('action', type=str, help='start/+/-')
args = parser.parse_args()

set_hepa_start(args.action)