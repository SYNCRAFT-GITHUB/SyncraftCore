import os
import yaml
import shutil
import subprocess
from git import Repo

pi = os.path.join('/home', 'pi')
core = os.path.join(pi, 'SyncraftCore')
py = 'apply.py'
sh = 'apply.sh'


class PATH:
    class STORE:
        PATH = os.path.join(core, 'store')
        KIAUH = os.path.join(core, 'store', 'kiauh')

        class STOCK:
            PATH = os.path.join(core, 'store', 'stock')
            KS = os.path.join(core, 'store', 'stock', 'KlipperScreen')
            PDC = os.path.join(core, 'store', 'stock', 'printerdataconfig')
            KLE = os.path.join(core, 'store', 'stock', 'klipper-led_effect')
            KLIPPER = os.path.join(core, 'store', 'stock', 'klipper')
            MOONRAKER = os.path.join(core, 'store', 'stock', 'moonraker')
            MAINSAIL = os.path.join(core, 'store', 'stock', 'mainsail')

        class FRESH:
            PATH = os.path.join(core, 'store', 'fresh')
            KS = os.path.join(core, 'store', 'fresh', 'KlipperScreen')
            PDC = os.path.join(core, 'store', 'fresh', 'printerdataconfig')
            KLE = os.path.join(core, 'store', 'fresh', 'klipper-led_effect')
            KLIPPER = os.path.join(core, 'store', 'fresh', 'klipper')
            MOONRAKER = os.path.join(core, 'store', 'fresh', 'moonraker')
            MAINSAIL = os.path.join(core, 'store', 'fresh', 'mainsail')

    class CACHE:
        PATH = os.path.join(core, 'cache')

        class CORE:
            PATH = os.path.join(core, 'cache', 'core')
            PDC = os.path.join(core, 'cache', 'core', 'printerdataconfig')
            KS = os.path.join(core, 'cache', 'core', 'KlipperScreen')
            KLE = os.path.join(core, 'cache', 'core', 'klipper-led_effect')
            KLIPPER = os.path.join(core, 'cache', 'core', 'klipper')
            MOONRAKER = os.path.join(core, 'cache', 'core', 'moonraker')
            MAINSAIL = os.path.join(core, 'cache', 'core', 'mainsail')

        class PDC:
            PATH = os.path.join(core, 'cache', 'pdc')

    class STATE:
        PATH = os.path.join(core, 'state')

        class UPGRADE:
            KS = os.path.join(core, 'state', 'upgrade', 'ks', sh)
            KLE = os.path.join(core, 'state', 'upgrade', 'kle', sh)
            MAINSAIL = os.path.join(core, 'state', 'upgrade', 'mainsail', sh)

    class CORE:
        PATH = os.path.join(core, 'core')
        INFO = os.path.join(core, 'core', 'info.yaml')
        UPDATE = os.path.join(core, 'core', 'update', py)
        CREATE = os.path.join(core, 'core', 'create', py)

    class PDC:
        PATH = os.path.join(core, 'pdc')
        MOONRAKER_CONF = PATH = os.path.join(core, 'pdc', 'moonraker.conf')


def model():
    with open(PATH.CORE.INFO, 'r') as prop:
        prop = yaml.safe_load(prop)
    return prop.get('model')


def branch(model: str, software: str):
    if '2' in model:
        n = '2'
    else:
        n = '1'

    if model == f'X{n}' and software == 'ks':
        return f'syncraftx{n}'
    if model == f'X1' and software == 'pdc':
        return f'syncraftx{n}'

    if model == f'X{n}-BETA' and software == 'ks':
        return f'syncraftx{n}-beta'
    if model == f'X{n}-BETA' and software == 'pdc':
        return f'syncraftx{n}-beta'

    if model == f'X{n}-DEV' and software == 'ks':
        return f'syncraftx{n}-dev'
    if model == f'X{n}-DEV' and software == 'pdc':
        return f'syncraftx{n}-dev'


def clone_in_path(repo_url, machine_dir, branch='master'):
    if os.path.exists(machine_dir):
        os.remove(machine_dir)
    print(f'Downloading from {repo_url}')
    Repo.clone_from(repo_url, machine_dir, branch=branch)


def distribute(to: str):
    print(f'Distributing from Cache to {to}.')
    for folder in os.listdir(PATH.CACHE.CORE.PATH):
        source = os.path.join(PATH.CACHE.CORE.PATH, folder)
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


clear_dir(PATH.CACHE.CORE.PATH)
clear_dir(PATH.STORE.FRESH.PATH)
clear_dir(PATH.STORE.STOCK.PATH)

create_dirs = [
    PATH.CACHE.CORE.MAINSAIL,
    PATH.STORE.FRESH.MAINSAIL,
    PATH.STORE.STOCK.MAINSAIL
]

for dir in create_dirs:
    if os.path.exists(dir):
        clear_dir(dir)
    else:
        os.makedirs(dir)


print('Downloading Mainsail')
git_profile = "https://github.com/SYNCRAFT-GITHUB"
repo_url = f"{git_profile}/mainsail/releases/latest/download/mainsail.zip"
unzip_cmd = "unzip -q mainsail.zip"
os.system(f"cd {PATH.CACHE.CORE.MAINSAIL} && wget -q {repo_url} && {unzip_cmd}")

clone_in_path("https://github.com/SYNCRAFT-GITHUB/KlipperScreen.git", PATH.CACHE.CORE.KS, branch(model(), 'ks'))
clone_in_path("https://github.com/SYNCRAFT-GITHUB/printerdataconfig.git", PATH.CACHE.CORE.PDC, branch(model(), 'pdc'))
clone_in_path("https://github.com/julianschill/klipper-led_effect", PATH.CACHE.CORE.KLE)
clone_in_path("https://github.com/SYNCRAFT-GITHUB/klipper.git", PATH.CACHE.CORE.KLIPPER)
clone_in_path("https://github.com/SYNCRAFT-GITHUB/moonraker.git", PATH.CACHE.CORE.MOONRAKER)
clone_in_path("https://github.com/SYNCRAFT-GITHUB/kiauh", PATH.STORE.KIAUH)

distribute(to=PATH.STORE.FRESH.PATH)

if os.path.exists(PATH.STORE.STOCK.PATH):
    if not os.listdir(PATH.STORE.STOCK.PATH):
        distribute(to=PATH.STORE.STOCK.PATH)
else:
    os.makedirs(PATH.STORE.STOCK.PATH)
    distribute(to=PATH.STORE.STOCK.PATH)

pi_as_owner(PATH.CACHE.CORE.PATH)
pi_as_owner(PATH.CACHE.PDC.PATH)
pi_as_owner(PATH.STORE.FRESH.PATH)

clear_dir(PATH.CACHE.CORE.PATH)
