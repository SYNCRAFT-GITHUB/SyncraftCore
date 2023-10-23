import os

state_dir = os.path.join('/home', 'pi', 'SyncraftCore', 'state')
upgrade_all = os.path.join(state_dir, 'upgrade', 'apply.sh')
upgrade_ks = os.path.join(state_dir, 'upgrade', 'ks', 'apply.sh')
upgrade_mainsail = os.path.join(state_dir, 'upgrade', 'mainsail', 'apply.sh')

machine_ks = os.path.join('/home', 'pi', 'KlipperScreen')

# Upgrade Mainsail
os.system(f'sudo bash {upgrade_mainsail}')

# Upgrade KS
os.system(f'sudo bash {upgrade_ks}')

if os.path.exists(machine_ks):
    os.system(f'sudo chown -R pi:1000 {machine_ks}')

os.system('sudo service KlipperScreen restart')