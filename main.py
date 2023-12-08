#!/usr/bin/env python3

import os

try:
    if not os.path.exists(DIR.PROP):
        os.system('sudo apt-get install python3-pip')
        os.system(f'pip3 install -r {DIR.REQ}')
except:
    pass

from operation import operations
from operation import Operation
import yaml
import random
import shutil
import subprocess
import socket
import requests
import time

alerts = []

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

class DIR:
    CORE = os.path.dirname(__file__)
    KIAUH = os.path.join(os.path.dirname(__file__), 'store', 'kiauh')
    SOFTWARES = os.path.join(os.path.dirname(__file__), 'store', 'fresh')
    STOCK = os.path.join(os.path.dirname(__file__), 'store', 'stock')
    PROP = os.path.join(os.path.dirname(__file__), 'core', 'info.yaml')
    REQ = os.path.join(os.path.dirname(__file__), 'core', 'requirements.txt')
    PACKAGES = os.path.join(os.path.dirname(__file__), 'machine', 'packages', 'apply.sh')
    ENV = os.path.join(os.path.dirname(__file__), 'env')

if not os.path.exists(DIR.SOFTWARES):
    os.makedirs(DIR.SOFTWARES)

if not os.path.exists(DIR.STOCK):
    os.makedirs(DIR.STOCK)

print ('\n➤ Check if there\'s missing packages in your system? (recommended) [y/n]:')
check_packages = input("➤ ")

if check_packages.lower()[0] == 'y':
    os.system(f'sudo bash {DIR.PACKAGES}')

if not os.path.exists(DIR.ENV):
    print(str(Color.MAGENTA + '[*] ' + Color.CYAN + 'Creating env...' + Color.RESET))
    os.system(f'python -m venv {DIR.ENV}')

if os.path.exists(DIR.ENV):
    os.system(f"source {os.path.join(DIR.ENV, 'bin', 'activate')}")

if os.path.exists(DIR.PROP):
    print(str(Color.MAGENTA + '[*] ' + Color.CYAN + 'info.yaml File OK' + Color.RESET))
else:
    data_index = {
        "model": "IDEX",
    }

    with open(DIR.PROP, 'w') as yaml_file:
        yaml.dump(data_index, yaml_file)
    print(str(Color.MAGENTA + '[*] ' + Color.CYAN + 'info.yaml File Created' + Color.RESET))
    
def internet():
    try:
        response = requests.get("https://www.google.com", timeout=5)
        return True
    except requests.ConnectionError:
        return False

def performAction(i: int):

    os.system('clear')

    if operations[i-1].web and internet() is False:
            print (Color.RED + 'INTERNET ACCESS IS REQUIRED!\n' + Color.RESET)
            return
    elif not operations[i-1].confirm:
        operations[i-1].apply()

    if operations[i-1].confirm:
        print (Color.MAGENTA + '| ' + Color.YELLOW + 'Action: ' + Color.BLUE + operations[i-1].desc + Color.RESET)
        print (Color.RED + '\nARE YOU SURE YOU WANT TO PERFORM THIS ACTION?' + Color.RESET)
        print(Color.YELLOW + '\nType \'CONFIRM\' TO PROCEED' + Color.RESET)
        print(Color.YELLOW + '\nType \'Q\' TO QUIT TO MAIN MENU' + Color.RESET)

        option = input(Color.CYAN + "\nOption: " + Color.RESET)
        if (option.upper() == "CONFIRM"):
            operations[i-1].apply()
        else:
            os.system('clear')
            return

def createAlerts():
    alerts.clear()
    try:
        if not os.listdir(DIR.KIAUH):
            alerts.append(str(Color.MAGENTA + '[!] ' + Color.RED + 'KIAUH DIRECTORY IS EMPTY' + Color.RESET))
    except:
        alerts.append(str(Color.MAGENTA + '[!] ' + Color.RED + 'KIAUH DIRECTORY NOT FOUND' + Color.RESET))
    if not os.listdir(DIR.SOFTWARES):
        alerts.append(str(Color.MAGENTA + '[!] ' + Color.RED + 'SOFTWARES DIRECTORY IS EMPTY' + Color.RESET))
    if not os.listdir(DIR.STOCK):
        alerts.append(str(Color.MAGENTA + '[!] ' + Color.RED + 'STOCK DIRECTORY IS EMPTY' + Color.RESET))

os.system('clear')

while (True):

    with open(DIR.PROP, 'r') as prop:
        prop = yaml.safe_load(prop)
    class PROP:
        MODEL = prop.get('model')

    hostname = socket.gethostname()
    last_date = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.path.getmtime(DIR.SOFTWARES)))
    createAlerts()

    logo: str = Color.YELLOW +  """
  ____                              __ _      ____               
 / ___| _   _ _ __   ___ _ __ __ _ / _| |_   / ___|___  _ __ ___ 
 \___ \| | | | '_ \ / __| '__/ _` | |_| __| | |   / _ \| '__/ _ |
  ___) | |_| | | | | (__| | | (_| |  _| |_  | |__| (_) | | |  __/
 |____/ \__, |_| |_|\___|_|  \__,_|_|  \__|  \____\___/|_|  \___|
        |___/                                                                                                           
    """ + Color.RESET

    logo_error: str = Color.RED +  """
                      ______
                   .-"      "-.
                  /            \\\tDO WE
                 |              |\tHAVE A
                 |,  .-.  .-.  ,|\tPROBLEM ?
                 | )(_o/  \o_)( |
                 |/     /\     \|
                                                                                                  
    """ + Color.RESET

    print(logo) if len(alerts) == 0 else print(logo_error)

    print (Color.MAGENTA + '\n| ' + Color.YELLOW + 'Model: ' + Color.BLUE + f'{PROP.MODEL}' + Color.RESET)

    if len(alerts) != 0:
        print(Color.MAGENTA + '\n[!] ' + Color.RED + 'SyncraftCore IS INCOMPLETE!\n' + Color.RESET)
        for alert in alerts:
            print(alert)
    else:
        print (Color.MAGENTA + '\n| ' + Color.YELLOW + 'Syncraft Host: ' + Color.BLUE + hostname + Color.RESET)
        print (Color.MAGENTA + '\n| ' + Color.YELLOW + 'Internet Access: ' + Color.BLUE + ('OK' if internet() else 'NOT DETECTED') + Color.RESET)
        print (Color.MAGENTA + '\n| ' + Color.YELLOW + 'Last Updated: ' + Color.BLUE + last_date + Color.RESET)

    print('')
    for i, operation in enumerate(operations):
        zero: str = '0'
        if i+1 >= 10:
            zero = ''
        if operation.web and internet() is False:
            print (Color.RED + f'| {zero}{i+1}\t-\t{operation.desc.upper()}' + Color.RESET)
        else:
            print (Color.MAGENTA + '| ' + Color.YELLOW + f'{zero}{i+1}' + Color.CYAN + '\t-\t' + Color.GREEN + f'{operation.desc}' + Color.RESET)

    print (Color.MAGENTA + '\n| ' + Color.YELLOW + '00' + Color.CYAN + '\t-\t' + Color.GREEN + 'Quit' + Color.RESET)

    try:
        option = int(input(Color.CYAN + "\nOption: " + Color.RESET))
        os.system('clear')
        if option == 0:
            break
        performAction(i=option)
    except:
        pass