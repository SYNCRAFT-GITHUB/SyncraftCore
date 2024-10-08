#!/usr/bin/env python3
from datetime import datetime
import socket
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from dirs import DIR

class Color:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    RESET = '\033[0m'

syncraftcore_dir = os.path.dirname(__file__)

if not os.path.exists(DIR.ENV.PATH):
    print(str(Color.MAGENTA + '[*] ' + Color.CYAN + 'Creating env...' + Color.RESET))
    os.system(f'python3 -m venv {DIR.ENV.PATH}')
    os.system(f"source {os.path.join(DIR.ENV.PATH, 'bin', 'activate')}")
else:
    os.system(f"source {os.path.join(DIR.ENV.PATH, 'bin', 'activate')}")

try:
    if not os.path.exists(DIR.CORE.INFO):
        os.system('sudo apt-get install python3-pip')
        os.system(f'pip3 install -r {DIR.CORE.REQUIREMENTS}')
except:
    print('Error trying to install python req.')
    pass

from core.create import create
from core.update import update
from core.set_main_canbus_uuid import set_main_canbus_uuid
from core.set_rp2040_one_uuid import set_rp2040_one_uuid
from core.set_rp2040_two_uuid import set_rp2040_two_uuid
import yaml
import random
import shutil
import subprocess
import socket
import requests
import time

for directory in [DIR.STORE.FRESH.PATH, DIR.STORE.STOCK.PATH, DIR.BACKUPS.PATH]:
    if not os.path.exists(directory):
        os.makedirs(directory)

print ('\n➤ Check if there\'s missing packages in your system? (recommended) [y/n]:')
check_packages = input("➤ ")

if 'y' in check_packages.lower():
    os.system(f'pip3 install -r {DIR.CORE.REQUIREMENTS}')

if os.path.exists(DIR.CORE.INFO):
    print(str(Color.MAGENTA + '[*] ' + Color.CYAN + 'info File OK' + Color.RESET))
else:
    data_index = {
        "model": "IDEX",
        "birth": datetime.now().strftime("%Y-%m-%d")
    }

    with open(DIR.CORE.INFO, 'w') as yaml_file:
        yaml.dump(data_index, yaml_file)
    print(str(Color.MAGENTA + '[*] ' + Color.CYAN + 'info.yaml File Created' + Color.RESET))
    
def internet():
    try:
        socket.create_connection(("www.github.com", 80))
        return True
    except:
        return False

def execute_bash(path: str, sudo=False, web=False):
    if web and internet():
        pass
    elif web and not internet():
        return None
    cmd = 'sudo bash' if sudo else 'bash'
    os.system(f"{cmd} {path}")

class Action:
    def __init__(self, title, function, arg=None):
        self.title = title
        self.function = function
        self.arg = arg

actions = [
    Action('Build', create),
    Action('Update Softwares Folder', update),
    Action('Upgrade Softwares', execute_bash, DIR.STATE.UPGRADE.APPLY),
    Action('Downgrade Softwares', execute_bash, DIR.STATE.DOWNGRADE.APPLY),
    Action('Reset Machine Properties', execute_bash, DIR.MACHINE.APPLY),
    Action('Install Python Req.', execute_bash, DIR.MACHINE.PYTHONREQ.APPLY),
    Action('Export Logs to USB', execute_bash, DIR.USB.EXPORT_LOGS),
    Action('Set Main Canbus UUID', set_main_canbus_uuid),
    Action('Set RP2040 (1) Canbus UUID', set_rp2040_one_uuid),
    Action('Set RP2040 (2) Canbus UUID', set_rp2040_two_uuid)
]

def alertMissing():

    check_dirs = [
        DIR.SYSTEM.KLIPPER.PATH,
        DIR.SYSTEM.MOONRAKER.PATH,
        DIR.SYSTEM.SV.PATH,
        DIR.SYSTEM.MAINSAIL.PATH,
        DIR.SYSTEM.PDC.PATH,
        DIR.STORE.KIAUH.PATH,
        DIR.STORE.FRESH.PATH,
        DIR.STORE.STOCK.PATH
    ]

    missing = []

    try:
        for path in check_dirs:
            if not os.path.exists(path):
                missing.append(path)
    except:
        pass

    if len(missing) >= 1:
        print(str(Color.YELLOW + '[!] ' + Color.RED + 'MISSING PIECES!' + Color.RESET))
        for item in missing:
            print(str(Color.YELLOW + '> ' + Color.RED + f'{item}' + Color.RESET))

os.system('clear')

while (True):

    with open(DIR.CORE.INFO, 'r') as prop:
        prop = yaml.safe_load(prop)
    class PROP:
        MODEL = prop.get('model')
        BIRTH = prop.get('birth')
        HEPA_COUNT = prop.get('hepa-count')

    hostname = socket.gethostname()
    last_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(DIR.STORE.FRESH.PATH)))

    logo: str = Color.YELLOW +  """
  ____                              __ _      ____               
 / ___| _   _ _ __   ___ _ __ __ _ / _| |_   / ___|___  _ __ ___ 
 \___ \| | | | '_ \ / __| '__/ _` | |_| __| | |   / _ \| '__/ _ |
  ___) | |_| | | | | (__| | | (_| |  _| |_  | |__| (_) | | |  __/
 |____/ \__, |_| |_|\___|_|  \__,_|_|  \__|  \____\___/|_|  \___|
        |___/                                                                                                           
    """ + Color.RESET

    print(logo)

    alertMissing()

    print (Color.MAGENTA + '\n| ' + Color.YELLOW + 'Model: ' + Color.BLUE + f'{PROP.MODEL}' + Color.RESET)
    print (Color.MAGENTA + '\n| ' + Color.YELLOW + 'Birth: ' + Color.BLUE + f'{PROP.BIRTH}' + Color.RESET)
    print (Color.MAGENTA + '\n| ' + Color.YELLOW + 'HEPA Counter: ' + Color.BLUE + f'{PROP.HEPA_COUNT}' + Color.RESET)
    print (Color.MAGENTA + '\n| ' + Color.YELLOW + 'Syncraft Host: ' + Color.BLUE + hostname + Color.RESET)
    print (Color.MAGENTA + '\n| ' + Color.YELLOW + 'Internet Access: ' + Color.BLUE + ('OK' if internet() else 'OFFLINE') + Color.RESET)
    print (Color.MAGENTA + '\n| ' + Color.YELLOW + 'Last Updated: ' + Color.BLUE + last_date + Color.RESET)

    print('')
    for i, action in enumerate(actions):
        print(Color.WHITE + f'[{i}] ' + Color.YELLOW + f'{action.title}' + Color.RESET)

    print(Color.YELLOW + f'\Querying canbus ids' + Color.RESET)
    subprocess.call(["python3", "/home/pi/katapult/scripts/flashtool.py", "-i", "can0", "-q"])

    print(Color.MAGENTA + '\n|' + Color.CYAN + ' Q ' + Color.RED + 'to Quit' + Color.RESET)

    user_input = input('\nACTION: ')

    if user_input.lower() == 'q':
        os.system('clear')
        exit()

    for i, action in enumerate(actions):
        if user_input == f'{i}':
            if action.arg is None:
                action.function()
            else:
                action.function(action.arg)
