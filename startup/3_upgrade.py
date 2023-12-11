from dirs import DIR
import os

# Upgrade Mainsail
os.system(f'sudo bash {DIR.STATE.UPGRADE.APPLY}')

# Upgrade KS
os.system(f'sudo bash {DIR.STATE.UPGRADE.KS.APPLY}')

if os.path.exists(machine_ks):
    os.system(f'sudo chown -R pi:1000 {DIR.SYSTEM.KS.PATH}')

os.system('sudo service KlipperScreen restart')