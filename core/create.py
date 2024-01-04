from dirs import DIR
from core.update import update
from startup.modules.transfer import transfer
import os

# rafaelSwi /*
# Calls all scripts and functions necessary
# to "create" the machine for the first time.

core = os.path.join('/home', 'pi', 'SyncraftCore')
class SCRIPT:
    DOWNLOAD = os.path.join(core, 'core', 'update', 'apply.py')
    UPGRADE = os.path.join(core, 'state', 'upgrade', 'apply.sh')
    MACHINE = os.path.join(core, 'machine', 'apply.sh')
    TRANSFER = os.path.join(core, 'startup', '1_transfer.py')

scripts = [
    DIR.STATE.UPGRADE.APPLY, DIR.MACHINE.APPLY
]

def create():

    update()

    for script in scripts:
        if '.py' in script:
            os.system(f'sudo python3 {script}')
        elif '.sh' in script:
            os.system(f'sudo bash {script}')

    transfer()