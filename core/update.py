import os
import yaml
import shutil
import subprocess
from git import Repo
from dirs import DIR

pi = os.path.join('/home', 'pi')
core = os.path.join(pi, 'SyncraftCore')
py = 'apply.py'
sh = 'apply.sh'

def model():
    with open(DIR.CORE.INFO, 'r') as prop:
        prop = yaml.safe_load(prop)
    return prop.get('model')

def clone_in_path(repo_url, machine_dir, branch='master'):
    if os.path.exists(machine_dir):
        shutil.rmtree(machine_dir)
    print(f'Downloading from {repo_url}')
    Repo.clone_from(repo_url, machine_dir, branch=branch)

def distribute(to: str):
    print(f'Distributing from Cache to {to}.')
    for folder in os.listdir(DIR.CACHE.CORE.PATH):
        source = os.path.join(DIR.CACHE.CORE.PATH, folder)
        destination = os.path.join(to, folder)
        if os.path.exists(source):
            if os.path.exists(destination):
                shutil.rmtree(destination)
            shutil.copytree(source, destination)

def clear_dir(dir: str):
    print(f'Cleaning {dir}')
    if os.path.exists(dir):
        shutil.rmtree(dir)
    os.makedirs(dir)
    pi_as_owner(dir)

def pi_as_owner(dir: str):
    if os.path.exists(dir):
        os.chown(dir, 1000, 1000)
        print(f'User "pi" now owns {dir}')

create_dirs = [
    DIR.CACHE.CORE.MAINSAIL.PATH,
    DIR.STORE.FRESH.MAINSAIL.PATH,
    DIR.STORE.STOCK.MAINSAIL.PATH
]

def update():

    print ('\n➤ Transfer downloaded softwares to the stock folder? [ y/n(default) ]')
    fill_stock = input("➤ ")

    if 'y' in fill_stock.lower():
        print('➤ YES\n')
        fill_stock = True
    else:
        print('➤ SKIP\n')
        fill_stock = False

    clear_dir(DIR.CACHE.CORE.PATH)
    clear_dir(DIR.STORE.FRESH.PATH)
    clear_dir(DIR.STORE.STOCK.PATH)

    for dir in create_dirs:
        if os.path.exists(dir):
            clear_dir(dir)
        else:
            os.makedirs(dir)

    print('Downloading Mainsail')
    git_profile = "https://github.com/SYNCRAFT-GITHUB"
    repo_url = f"{git_profile}/mainsail/releases/latest/download/mainsail.zip"
    unzip_cmd = "unzip -q mainsail.zip"
    os.system(f"cd {DIR.CACHE.CORE.MAINSAIL} && wget -q {repo_url} && {unzip_cmd}")

    clone_in_path("https://github.com/SYNCRAFT-GITHUB/KlipperScreenIDEX.git", DIR.CACHE.CORE.KS)
    clone_in_path("https://github.com/SYNCRAFT-GITHUB/IDEXConfig.git", DIR.CACHE.CORE.)
    clone_in_path("https://github.com/SYNCRAFT-GITHUB/klipper-led_effect", DIR.CACHE.CORE.KLE.PATH)
    clone_in_path("https://github.com/SYNCRAFT-GITHUB/klipper.git", DIR.CACHE.CORE.KLIPPER.PATH)
    clone_in_path("https://github.com/SYNCRAFT-GITHUB/moonraker.git", DIR.CACHE.CORE.MOONRAKER.PATH)
    clone_in_path("https://github.com/SYNCRAFT-GITHUB/kiauh", DIR.STORE.KIAUH.PATH)

    distribute(to=DIR.STORE.FRESH.PATH)

    if os.path.exists(DIR.STORE.STOCK.PATH):
        if fill_stock:
            distribute(to=DIR.STORE.STOCK.PATH)
    else:
        os.makedirs(DIR.STORE.STOCK.PATH)
        distribute(to=DIR.STORE.STOCK.PATH)

    pi_as_owner(DIR.CACHE.CORE.PATH)
    pi_as_owner(PATH.CACHE.PDC.PATH)
    pi_as_owner(DIR.STORE.FRESH.PATH)

    clear_dir(DIR.CACHE.CORE.PATH)