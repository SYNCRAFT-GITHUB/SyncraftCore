import os
import shutil

name = '[TRANSFER SCRIPT]'
saveconfig_line: str = '#*# <---------------------- SAVE_CONFIG ---------------------->'
saveconfig_backup = [
    '#*# <---------------------- SAVE_CONFIG ---------------------->',
    '#*# DO NOT EDIT THIS BLOCK OR BELOW. The contents are auto-generated.',
    '#*#',
    '#*# [probe]',
    '#*# z_offset = -0.300',
    '#*#',
    '#*# [stepper_z]',
    '#*# position_endstop = 340.25',
]

core = os.path.join('/home', 'pi', 'SyncraftCore')
pdc = os.path.join ('/home', 'pi', 'printer_data', 'config')

class PATH:
    CORE = core
    PDC_FRESH = os.path.join(core, 'store', 'fresh', 'printerdataconfig')
    PDC_MACHINE = pdc
    PDC_CACHE = os.path.join(core, 'cache', 'pdc')
    class FILE:
        class PDC_FRESH_BACKUP:
            KS = os.path.join(core, 'store', 'fresh', 'printerdataconfig', 'backups', 'backup-KlipperScreen.conf')
            VARIABLES = os.path.join(core, 'store', 'fresh', 'printerdataconfig', 'backups', 'backup-variables.cfg')
            PRINTER = os.path.join(core, 'store', 'fresh', 'printerdataconfig', 'backups', 'backup-printer.cfg')
        class PDC_BACKUP:
            KS = os.path.join(pdc, 'backups', 'backup-KlipperScreen.conf')
            VARIABLES = os.path.join(pdc, 'backups', 'backup-variables.cfg')
            PRINTER = os.path.join(pdc, 'backups', 'backup-printer.cfg')
        class CACHE:
            KS = os.path.join(core, 'cache', 'pdc', 'KlipperScreen.conf')
            VARIABLES = os.path.join(core, 'cache', 'pdc', 'variables.cfg')
            PRINTER = os.path.join (core, 'cache', 'pdc', 'printer.cfg')
        class MACHINE:
            KS = os.path.join(pdc, 'KlipperScreen.conf')
            VARIABLES = os.path.join(pdc, 'variables.cfg')
            PRINTER = os.path.join (pdc, 'printer.cfg')

class BOOL:
    SAVE_LINES = False

extracted_saveconfig = []

# DELETE ALL CONTENT ON PDC CACHE
if os.path.exists(PATH.PDC_CACHE):
    print(f'{name} ✓ Deleting all content in PDC Cache.')
    shutil.rmtree(PATH.PDC_CACHE)
else:
    print(f"{name} ☓ PDC Cache not found. Creating it.")
    try:
        os.makedirs(PATH.PDC_CACHE)
    except:
        print(f"{name} ☓ Error trying to create PDC Cache Path, maybe a permission error?")
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
    with open(PATH.FILE.CACHE.PRINTER, 'w') as extracted:
        if (BOOL.SAVE_LINES):
            extracted.writelines(extracted_saveconfig)
            print(f'{name} ✓ Successfully extracted SaveConfig Lines from PDC Machine to PDC Cache.')
        else:
            extracted.writelines(saveconfig_backup)
            print(f'{name} ✓ Used Default Values to write the contents of SaveConfig.')
except:
    print(f'{name} ☓ Error trying to open/create the Printer File in PDC Cache.')
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
    except:
        print(f"{name} ☓ Error trying to create PDC Machine Path, maybe a permission error?")
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
except:
    print(f"{name} ☓ Error trying to copy files from Cache to PDC Machine.")
    exit()

# TRANSFORM 'BACKUP' PRINTER.CFG FILE INTO USEFUL FILE
try:
    shutil.copyfile(PATH.FILE.PDC_BACKUP.PRINTER, PATH.FILE.MACHINE.PRINTER)
    print(print(f'{name} ✓ PDC Machine Backup Printer file transformed into normal file.'))
except:
    print(print(f'{name} ☓ Error trying to transform PDC Machine Backup Printer File into normal file.'))
    exit()

# APPEND CONTENT TO THAT PRINTER.CFG FILE
try:
    with open(PATH.FILE.MACHINE.PRINTER, 'a') as printer_cfg:
        with open(PATH.FILE.CACHE.PRINTER, 'r') as extracted:
            printer_cfg.write('\n')
            for line in extracted:
                printer_cfg.write(line)
    print(print(f'{name} ✓ Added SaveConfig content to PDC Machine Printer file.'))
except:
    print(print(f'{name} ☓ Error while trying to append SaveConfig content into PDC Machine Printer File'))

# MAKE SURE THAT USER 'pi' OWNS THE MACHINE PATH
try:
    os.chown(PATH.PDC_MACHINE, 1000, 1000)
    print(print(f'{name} ✓ User \'pi\' now owns PDC Machine Directory.'))
except:
    print(print(f'{name} ☓ User \'pi\' can\'t own PDC Machine Directory.'))