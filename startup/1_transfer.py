import configparser
import subprocess
import shutil
import yaml
import os

name = '[TRANSFER SCRIPT]'
saveconfig_line: str = '#*# <---------------------- SAVE_CONFIG ---------------------->'
saveconfig_backup = """
#*# <---------------------- SAVE_CONFIG ---------------------->
#*# DO NOT EDIT THIS BLOCK OR BELOW. The contents are auto-generated.
#*#
#*# [probe]
#*# z_offset = -0.300
#*#
#*# [stepper_z]
#*# position_endstop = 340.25
"""

core = os.path.join('/home', 'pi', 'SyncraftCore')
pdc = os.path.join ('/home', 'pi', 'printer_data', 'config')

class PATH:
    CORE = core
    PDC_FRESH = os.path.join(core, 'store', 'fresh', 'IDEXConfig')
    PDC_MACHINE = pdc
    PDC_CACHE = os.path.join(core, 'cache', 'pdc')
    MOONRAKER = os.path.join('/home', 'pi', 'moonraker')
    KLIPPER = os.path.join('/home', 'pi', 'klipper')
    MAINSAIL = os.path.join('/home', 'pi', 'mainsail')
    class SCRIPT:
        OVERWRITE = os.path.join(core, 'pdc', 'apply.sh')
    class FILE:
        class PDC_FRESH_BACKUP:
            KS = os.path.join(core, 'store', 'fresh', 'IDEXConfig', 'backups', 'KlipperScreen.conf')
            VARIABLES = os.path.join(core, 'store', 'fresh', 'IDEXConfig', 'backups', 'variables.cfg')
            PRINTER = os.path.join(core, 'store', 'fresh', 'IDEXConfig', 'backups', 'printer.cfg')
        class PDC_BACKUP:
            KS = os.path.join(pdc, 'backups', 'KlipperScreen.conf')
            VARIABLES = os.path.join(pdc, 'backups', 'variables.cfg')
            PRINTER = os.path.join(pdc, 'backups', 'printer.cfg')
        class CACHE:
            KS = os.path.join(core, 'cache', 'pdc', 'KlipperScreen.conf')
            VARIABLES = os.path.join(core, 'cache', 'pdc', 'variables.cfg')
            PRINTER = os.path.join (core, 'cache', 'pdc', 'printer.cfg')
        class MACHINE:
            KS = os.path.join(pdc, 'KlipperScreen.conf')
            VARIABLES = os.path.join(pdc, 'variables.cfg')
            PRINTER = os.path.join (pdc, 'printer.cfg')
        class CORE:
            PROP = os.path.join(core, 'core', 'info.yaml')

class BOOL:
    SAVE_LINES = False

extracted_saveconfig = []

def securePermission ():
    dirs = [PATH.CORE, PATH.PDC_MACHINE, PATH.MAINSAIL]
    for path in dirs:
        try:
            for dirpath, dirnames, filenames in os.walk(path):
                shutil.chown(dirpath, 1000, 1000)
                for filename in filenames:
                    shutil.chown(os.path.join(dirpath, filename), 1000, 1000)
        except Exception as e:
            print(f"{name} ☓ User 'pi' can't own '{path}'.")
            print(f"{name} {e}")

securePermission()

# DELETE ALL CONTENT ON PDC CACHE
if os.path.exists(PATH.PDC_CACHE):
    print(f'{name} ✓ Deleting all content in PDC Cache.')
    shutil.rmtree(PATH.PDC_CACHE)
else:
    print(f"{name} ☓ PDC Cache not found. Creating it.")
    try:
        os.makedirs(PATH.PDC_CACHE)
    except Exception as e:
        print(f"{name} ☓ Error trying to create PDC Cache Path, maybe a permission error?")
        print(f"{name} {e}")
        exit()

# TRY TO FIND THE SAVECONFIG LINE IN PRINTER.CFG
if os.path.exists(PATH.FILE.MACHINE.PRINTER):
    with open(PATH.FILE.MACHINE.PRINTER, 'r') as printer_cfg:

        for i, line in enumerate(printer_cfg):
            if saveconfig_line in line:
                BOOL.SAVE_LINES = True
                print(f'{name} ✓ SaveConfig Line found in MACHINE PDC Printer File. Saving content...')
            if BOOL.SAVE_LINES:
                extracted_saveconfig.append(line)

    if (not BOOL.SAVE_LINES):
        print(f'{name} ☓ Printer File found in MACHINE PDC, but no SaveConfig Line. Using SaveConfig Line Default Values.')

else:
    print(f'{name} ☓ No Printer file found in MACHINE PDC. Using SaveConfig Line Default Values.')

# CREATE A FILE IN CACHE AND WRITE IT'S LINES BASED ON THE EXTRACTED SAVECONFIG LINE
try:
    if not os.path.exists(PATH.PDC_CACHE):
        os.makedirs(PATH.PDC_CACHE)
        print(f'{name} ✓ Created PDC Cache.')
except Exception as e:
    print(f'{name} ☓ Error trying to create PDC Cache.')
    print(f"{name} {e}")
    exit()
try:
    with open(PATH.FILE.CACHE.PRINTER, 'w') as extracted:
        if (BOOL.SAVE_LINES):
            extracted.writelines(extracted_saveconfig)
            print(f'{name} ✓ Successfully extracted SaveConfig Lines from PDC Machine to PDC Cache.')
        else:
            extracted.writelines(saveconfig_backup)
            print(f'{name} ✓ Used Default Values to write the contents of SaveConfig.')
except Exception as e:
    print(f'{name} ☓ Error trying to open/create the Printer File in PDC Cache.')
    print(f"{name} {e}")
    exit()

# COPY BOTH KLIPPERSCREEN.CONF AND VARIABLES.CFG TO PDC CACHE
if os.path.exists(PATH.FILE.MACHINE.KS):
    shutil.copyfile(PATH.FILE.MACHINE.KS, PATH.FILE.CACHE.KS)
    print(f'{name} ✓ KS Machine PDC File copied to PDC Cache.')
elif os.path.exists(PATH.FILE.PDC_BACKUP.KS):
    print(f'{name} ☓ KS Machine PDC Not found.')
    shutil.copyfile(PATH.FILE.PDC_BACKUP.KS, PATH.FILE.CACHE.KS)
    print(f'{name} ✓ KS Machine PDC (Backup) File copied to PDC Cache.')
elif os.path.exists(PATH.FILE.PDC_FRESH_BACKUP.KS):
    print(f'{name} ☓ KS Machine PDC (Backup) Not found.')
    shutil.copyfile(PATH.FILE.PDC_FRESH_BACKUP.KS, PATH.FILE.CACHE.KS)
    print(f'{name} ✓ KS Fresh PDC (Backup) File copied to PDC Cache.')
else:
    print(f'{name} ☓ No KS Backup file found at all.')
    exit()

if os.path.exists(PATH.FILE.MACHINE.VARIABLES):
    shutil.copyfile(PATH.FILE.MACHINE.VARIABLES, PATH.FILE.CACHE.VARIABLES)
    print(f'{name} ✓ Variables Machine PDC File copied to PDC Cache.')
elif os.path.exists(PATH.FILE.PDC_BACKUP.VARIABLES):
    print(f'{name} ☓ Variables Machine PDC Not found.')
    shutil.copyfile(PATH.FILE.PDC_BACKUP.VARIABLES, PATH.FILE.CACHE.VARIABLES)
    print(f'{name} ✓ Variables Machine PDC (Backup) File copied to PDC Cache.')
elif os.path.exists(PATH.FILE.PDC_FRESH_BACKUP.VARIABLES):
    print(f'{name} ☓ Variables Machine PDC (Backup) Not found.')
    shutil.copyfile(PATH.FILE.PDC_FRESH_BACKUP.VARIABLES, PATH.FILE.CACHE.VARIABLES)
    print(f'{name} ✓ Variables Fresh PDC (Backup) File copied to PDC Cache.')
else:
    print(f'{name} ☓ No Variables Backup file found at all.')
    exit()

# DELETE ALL CONTENT ON PRINTER_DATA/CONFIG
if os.path.exists(PATH.PDC_MACHINE):
    print(f'{name} ✓ Deleting all content in PDC Machine.')
    shutil.rmtree(PATH.PDC_MACHINE)
else:
    print(f"{name} ☓ PDC Machine not found. This really should't happen... Creating it.")
    try:
        os.makedirs(PATH.PDC_MACHINE)
    except Exception as e:
        print(f"{name} ☓ Error trying to create PDC Machine Path, maybe a permission error?")
        print(f"{name} {e}")
        exit()

# TRANSFER ALL CONTENT FROM PDC_FRESH TO MACHINE
if os.path.exists(PATH.PDC_FRESH):
    shutil.copytree(PATH.PDC_FRESH, PATH.PDC_MACHINE)
    print(print(f'{name} ✓ Transferred all content from PDC Fresh to PDC Machine.'))
else:
    print(f'{name} ☓ No Fresh PDC Available.')
    exit()

# COPY BOTH KLIPPERSCREEN.CONF AND VARIABLES.CFG TO PDC MACHINE
try:
    shutil.copyfile(PATH.FILE.CACHE.KS, PATH.FILE.MACHINE.KS)
    shutil.copyfile(PATH.FILE.CACHE.VARIABLES, PATH.FILE.MACHINE.VARIABLES)
    print(print(f'{name} ✓ Transferred both KS and Variables Files from PDC Cache to PDC Machine.'))
except Exception as e:
    print(f"{name} ☓ Error trying to copy files from Cache to PDC Machine.")
    print(f"{name} {e}")
    exit()

# INSERT CANBUS UUID INTO PRINTER.CFG
try:
    config = configparser.ConfigParser()
    config.read(PATH.FILE.PDC_BACKUP.PRINTER)
    if config.has_section('mcu') and config.has_option('mcu', 'canbus_uuid'):
        with open(PATH.FILE.CORE.PROP, 'r') as prop_file:
            data = yaml.safe_load(prop_file)
            config.set('mcu', 'canbus_uuid', data['canbus_uuid'])
            with open (PATH.FILE.PDC_BACKUP.PRINTER, 'w') as printercfg_file:
                config.write(printercfg_file)
                print(print(f'{name} ✓ PDC Machine Backup Printer file now has updated Canbus UUID.'))
except Exception as e:
    print(print(f'{name} ☓ Error trying to update Canbus UUID in printer cfg file.'))

# TRANSFORM 'BACKUP' PRINTER.CFG FILE INTO USEFUL FILE
try:
    shutil.copyfile(PATH.FILE.PDC_BACKUP.PRINTER, PATH.FILE.MACHINE.PRINTER)
    print(print(f'{name} ✓ PDC Machine Backup Printer file transformed into normal file.'))
except Exception as e:
    print(print(f'{name} ☓ Error trying to transform PDC Machine Backup Printer File into normal file.'))
    print(f"{name} {e}")
    exit()

# APPEND CONTENT TO THAT PRINTER.CFG FILE
try:
    with open(PATH.FILE.MACHINE.PRINTER, 'a') as printer_cfg:
        with open(PATH.FILE.CACHE.PRINTER, 'r') as extracted:
            printer_cfg.write('\n')
            for line in extracted:
                printer_cfg.write(line)
    print(print(f'{name} ✓ Added SaveConfig content to PDC Machine Printer file.'))
except Exception as e:
    print(print(f'{name} ☓ Error while trying to append SaveConfig content into PDC Machine Printer File'))
    print(f"{name} {e}")

# OVERWRITE FILES ON MACHINE PDC
subprocess.run(['sudo', 'bash', PATH.SCRIPT.OVERWRITE], check=True)

securePermission()