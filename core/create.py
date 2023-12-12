from dirs import DIR
from core.update import update
import os

core = os.path.join('/home', 'pi', 'SyncraftCore')
class SCRIPT:
    DOWNLOAD = os.path.join(core, 'core', 'update', 'apply.py')
    UPGRADE = os.path.join(core, 'state', 'upgrade', 'apply.sh')
    MACHINE = os.path.join(core, 'machine', 'apply.sh')
    TRANSFER = os.path.join(core, 'startup', '1_transfer.py')

scripts = [
    DIR.STATE.UPGRADE.APPLY, DIR.MACHINE.APPLY, DIR.STARTUP.GET_FROM_TERM('transfer')
]

def create():

    update()

    for script in scripts:
        if '.py' in script:
            os.system(f'sudo python3 {script}')
        elif '.sh' in script:
            os.system(f'sudo bash {script}')