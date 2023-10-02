import os

state_dir = os.path.join('/home', 'pi', 'SyncraftCore', 'state')
upgrade_all = os.path.join(state_dir, 'upgrade', 'apply.sh')
upgrade_ks = os.path.join(state_dir, 'upgrade', 'ks', 'apply.sh')
upgrade_mainsail = os.path.join(state_dir, 'upgrade', 'mainsail', 'apply.sh')

# Upgrade Mainsail
os.system(f'sudo bash {upgrade_mainsail}')

# Upgrade KS
os.system(f'sudo bash {upgrade_ks}')
os.system('sudo service KlipperScreen restart')