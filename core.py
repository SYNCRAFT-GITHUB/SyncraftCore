from operation import operations
from operation import Operation
import yaml
import os
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

if not os.path.exists(DIR.SOFTWARES):
    os.mkdir(DIR.SOFTWARES)

if not os.path.exists(DIR.STOCK):
    os.mkdir(DIR.STOCK)

if os.path.exists(DIR.PROP):
    print(str(Color.MAGENTA + '[*] ' + Color.CYAN + 'properties.yaml File OK' + Color.RESET))
else:
    data_index = {
        "model": "X1",
    }

    with open(DIR.PROP, 'w') as yaml_file:
        yaml.dump(data_index, yaml_file)
    print(str(Color.MAGENTA + '[*] ' + Color.CYAN + 'properties.yaml File Created' + Color.RESET))
    
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
  ____                              __ _      ____               
 /___|   _ __   ___ _ __ __ _ /_| |_   /___\t|___  _ __ ___ 
 \___ \t\  | |\t ' \ /\t_| \t'__/ _` | |_| __| |    /_ \t '__/ _ |
  _) \t| ||  | || |(_|  (_| | _| \t|_ | |_\t_| _) || |  __/
 |___/ \__,_|\t |_\__\t|  \__,_|_|  \__|  \____\__\t_/||  \___|
        |__/                                                                                                           
    """ + Color.RESET

    print(logo) if len(alerts) == 0 else print(logo_error)

    print (Color.MAGENTA + '\n| ' + Color.YELLOW + 'Model: ' + Color.BLUE + PROP.MODEL + Color.RESET)

    if len(alerts) != 0:
        print(Color.MAGENTA + '\n[!] ' + Color.RED + 'SyncraftCore IS NOT READY!\n' + Color.RESET)
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