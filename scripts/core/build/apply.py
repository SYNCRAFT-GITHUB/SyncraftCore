core_dir = os.path.join('/home', 'pi', 'Syncraftcore_dir')
scripts_dir = os.path.join(core_dir, 'scripts')

class DIR:
    DOWNLOAD_ALL = os.path.join(scripts_dir, 'core', 'download', 'apply.py')
    UPDATE_ALL = os.path.join(scripts_dir, 'maintenance', 'update', 'apply.sh')
    TRANSFER = os.path.join(core_dir, 'startup', 'transfer.py')

scripts = [DIR.DOWNLOAD_ALL, DIR.UPDATE_ALL, DIR.TRANSFER]

for script in scripts:
    if '.py' in script:
        os.system(f'sudo python3 {script}')
    elif '.sh' in script:
        os.system(f'sudo bash {script}')
