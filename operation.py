import os
import shutil
import subprocess

core = os.getcwd()

class Operation:
    def __init__(self, desc, path, format, script='apply', sudo=False, web=False, confirm=False, args={}):
        self.desc = desc
        self.path = path
        self.format = format
        self.script = script
        self.sudo = sudo
        self.web = web
        self.confirm = confirm
        self.args = args

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
            execute = f'sudo {full_cmd}'
            if self.sudo:
                execute = f'sudo {full_cmd}'
            else:
                execute = full_cmd

            if (self.args != {}):

                for key, value in self.args.items():
                    execute += f' --{key} "{value}"'

            os.system(execute)

operations = [

    Operation('Switch to Kiauh', os.path.join(core, 'store', 'kiauh'), 'sh', script='kiauh'),

    Operation('Update Softwares Folder', os.path.join(core, 'core', 'update'), 'py', sudo=True, web=True),
    Operation('Upgrade Softwares', os.path.join(core, 'state', 'upgrade'), 'sh'),
    Operation('Downgrade Softwares', os.path.join(core, 'state', 'downgrade'), 'sh'),

    Operation('Reset Machine Properties', os.path.join(core, 'machine'), 'sh'),

    Operation('Export Logs to USB', os.path.join(core, 'usb', 'logs'), 'sh'),
    Operation('Export Slicer Pack to USB', os.path.join(core, 'usb', 'slicer'), 'sh'),

    Operation('Build', os.path.join(core, 'core', 'create'), 'py', web=True, confirm=True),
]