import os
import shutil
import subprocess

core = os.getcwd()

class Operation:
    def __init__(self, desc, path, format, script='apply', sudo=False, web=False, confirm=False):
        self.desc = desc
        self.path = path
        self.format = format
        self.script = script
        self.sudo = sudo
        self.web = web
        self.confirm = confirm

    def apply(self):
        command: str
        if self.format == 'sh':
            command = 'bash'
        else:
            command = 'python3'
        script_full_path = os.path.join(self.path, f"{self.script}.{self.format}")

        full_cmd: str
        if os.path.exists(script_full_path):
            full_cmd = f'{command} {script_full_path}'
            if self.sudo:
                os.system(f'sudo {full_cmd}')
            else:
                os.system(full_cmd)

operations = [

    Operation('Set to Syncraft X1', os.path.join(core, 'scripts', 'core', 'properties', 'model', 'X1'), 'py'),
    Operation('Set to Syncraft X2', os.path.join(core, 'scripts', 'core', 'properties', 'model', 'X2'), 'py'),

    Operation('Switch to Kiauh', os.path.join(core, 'scripts', 'kiauh'), 'sh', script='kiauh'),

    Operation('Update Softwares Folder', os.path.join(core, 'scripts', 'core', 'update'), 'py', sudo=True, web=True),

    Operation('Reset Machine Properties', os.path.join(core, 'machine'), 'sh'),

    Operation('Export Logs to USB', os.path.join(core, 'scripts', 'pdc', 'logs', 'usb'), 'sh'),
    Operation('Export Slicer Pack to USB', os.path.join(core, 'slicer'), 'py'),

    Operation('Update KlipperScreen', os.path.join(core, 'scripts', 'maintenance', 'update', 'klipperscreen'), 'sh'),
    Operation('Update Mainsail', os.path.join(core, 'scripts', 'maintenance', 'update', 'mainsail'), 'sh'),
    Operation('Update Printerdataconfig', os.path.join(core, 'scripts', 'pdc', 'update'), 'sh'),
    Operation('Update Moonraker', os.path.join(core, 'scripts', 'maintenance', 'update', 'moonraker'), 'sh'),
    Operation('Update Klipper LED Effects', os.path.join(core, 'scripts', 'maintenance', 'update', 'kle'), 'sh'),

    Operation('Downgrade KlipperScreen', os.path.join(core, 'scripts', 'maintenance', 'revert', 'klipperscreen'), 'sh'),
    Operation('Downgrade Mainsail', os.path.join(core, 'scripts', 'maintenance', 'revert', 'mainsail'), 'sh'),
    Operation('Downgrade Printerdataconfig', os.path.join(core, 'scripts', 'pdc', 'revert'), 'py'),
    Operation('Downgrade Moonraker', os.path.join(core, 'scripts', 'maintenance', 'revert', 'moonraker'), 'sh'),
    Operation('Downgrade Klipper LED Effects', os.path.join(core, 'scripts', 'maintenance', 'revert', 'kle'), 'sh'),

    Operation('Download All (replace stock)', os.path.join(core, 'scripts', 'core', 'download'), 'py', sudo=True, web=True, confirm=True),
]