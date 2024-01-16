from dirs import DIR
import os

# rafaelSwi /*
# Transfers the latest software saved on the machine
# to the execution directories where they should normally be.

def upgrade():

    # Upgrade Mainsail
    os.system(f'sudo bash {DIR.STATE.UPGRADE.APPLY}')

    # Upgrade SV
    os.system(f'sudo bash {DIR.STATE.UPGRADE.SV.APPLY}')

    if os.path.exists(DIR.SYSTEM.SV.PATH):
        os.system(f'sudo chown -R pi:1000 {DIR.SYSTEM.SV.PATH}')

    os.system('sudo service SwierVision restart')