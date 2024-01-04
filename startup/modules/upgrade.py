from dirs import DIR
import os

# rafaelSwi /*
# Transfers the latest software saved on the machine
# to the execution directories where they should normally be.

def upgrade():

    # Upgrade Mainsail
    os.system(f'sudo bash {DIR.STATE.UPGRADE.APPLY}')

    # Upgrade KS
    os.system(f'sudo bash {DIR.STATE.UPGRADE.KS.APPLY}')

    if os.path.exists(DIR.SYSTEM.KS.PATH):
        os.system(f'sudo chown -R pi:1000 {DIR.SYSTEM.KS.PATH}')

    os.system('sudo service KlipperScreen restart')