import os
import yaml
import shutil
import subprocess
from git import Repo

core: str = os.path.join("/home/pi", "SyncraftCore")

yaml_path = os.path.join(core, 'properties.yaml')
with open(yaml_path, 'r') as prop:
        prop = yaml.safe_load(prop)
model = prop.get('model')

if model == 'X1':
    scx_branch = 'syncraftx1'
elif model == 'X2':
    scx_branch = 'syncraftx2'

cache_dir = os.path.join(core, "cache", "core")
mainsail_location = os.path.join(cache_dir, 'mainsail')
git_profile = "https://github.com/SYNCRAFT-GITHUB"
repo_url = f"{git_profile}/mainsail/releases/latest/download/mainsail.zip"
unzip_cmd = "unzip -q mainsail.zip"

if os.path.exists(cache_dir):
    shutil.rmtree(cache_dir)

os.mkdir(cache_dir)
os.mkdir(mainsail_location)

print ('Downloading Mainsail')
os.system (f"cd {mainsail_location} && wget -q {repo_url} && {unzip_cmd}")
print ('Downloading KS')
repo_url = "https://github.com/SYNCRAFT-GITHUB/KlipperScreen.git"
Repo.clone_from(repo_url, os.path.join(cache_dir, 'KlipperScreen'), branch=scx_branch)
print ('Downloading PDC')
repo_url = "https://github.com/SYNCRAFT-GITHUB/printerdataconfig.git"
Repo.clone_from(repo_url, os.path.join(cache_dir, 'printerdataconfig'), branch=scx_branch)
print ('Downloading Klipper')
repo_url = "https://github.com/SYNCRAFT-GITHUB/klipper.git"
Repo.clone_from(repo_url, os.path.join(cache_dir, 'klipper'), branch="master")
print ('Downloading Moonraker')
repo_url = "https://github.com/SYNCRAFT-GITHUB/moonraker.git"
Repo.clone_from(repo_url, os.path.join(cache_dir, 'moonraker'), branch="master")
print ('Downloading KLE')
repo_url = "https://github.com/julianschill/klipper-led_effect"
Repo.clone_from(repo_url, os.path.join(cache_dir, 'klipper-led_effect'), branch="master")
print ('Done downloading')

print('Started file distribution on softwares folder')
for folder in os.listdir(cache_dir):
    
    source = os.path.join(cache_dir, folder)
    destination = os.path.join(core, "softwares", folder)
    if os.path.exists(source):
        if os.path.exists(destination):
            shutil.rmtree(destination)
        shutil.copytree(source, destination)
print ('Finished file distribution')

print ('Downloading Kiauh')
repo_url = "https://github.com/SYNCRAFT-GITHUB/kiauh"
Repo.clone_from(repo_url, os.path.join(cache_dir, 'kiauh'), branch="master")
source = os.path.join(cache_dir, 'kiauh')
destination = os.path.join(core, "scripts", "kiauh")
if os.path.exists(source):
    if os.path.exists(destination):
        shutil.rmtree(destination)
    shutil.copytree(source, destination)

print ('Adjusting usage permissions')
os.chown(cache_dir, 1000, 1000)
os.chown(softwares_dir, 1000, 1000)
os.chown(stock_dir, 1000, 1000)
print ('Done adjusting usage permissions')

print('Done.\nReseting cache...')
shutil.rmtree(cache_dir)
os.mkdir(cache_dir)