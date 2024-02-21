from dirs import DIR
import configparser
import subprocess
import shutil
import yaml
import os

# rafaelSwi /*
# This script replaces the klipper config folder saved on the machine with a
# more recent version saved on the machine, saving the properties of
# some files (such as printer.cfg parameters) and KS/SV settings.
# It also applies the canbus UUID to printer.cfg before transferring it.

def transfer():

    name = '[TRANSFER SCRIPT]'
    saveconfig_line = '#*# <---------------------- SAVE_CONFIG ---------------------->'
    saveconfig_backup = """
#*# <---------------------- SAVE_CONFIG ---------------------->
#*# DO NOT EDIT THIS BLOCK OR BELOW. The contents are auto-generated.
#*#
#*# [probe]
#*# z_offset = -0.300
#*#
#*# [bed_mesh default]
#*# version = 1
#*# points =
#*# 	  0.066457, 0.065623, 0.055623, 0.042811
#*# 	  0.020519, 0.031561, 0.041353, 0.022811
#*# 	  -0.052293, 0.051248, 0.026248, -0.056356
#*# 	  -0.035418, 0.051144, 0.047186, -0.094793
#*# x_count = 4
#*# y_count = 4
#*# mesh_x_pps = 2
#*# mesh_y_pps = 2
#*# algo = bicubic
#*# tension = 0.2
#*# min_x = 30.0
#*# max_x = 270.0
#*# min_y = 30.0
#*# max_y = 270.0
    """

    save_lines: bool = False
    extracted_saveconfig = []

    def securePermission ():
        dirs = [DIR.PATH, DIR.SYSTEM.PDC.PATH, DIR.SYSTEM.MAINSAIL.PATH]
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
    if os.path.exists(DIR.CACHE.CORE.PDC.PATH):
        print(f'{name} ✓ Deleting all content in PDC Cache.')
        shutil.rmtree(DIR.CACHE.CORE.PDC.PATH)
    else:
        print(f"{name} ☓ PDC Cache not found. Creating it.")
        try:
            os.makedirs(DIR.CACHE.CORE.PDC.PATH)
        except Exception as e:
            print(f"{name} ☓ Error trying to create PDC Cache Path, maybe a permission error?")
            print(f"{name} {e}")
            exit()

    # TRY TO FIND THE SAVECONFIG LINE IN PRINTER.CFG
    if os.path.exists(DIR.SYSTEM.PDC.PRINTER):
        with open(DIR.SYSTEM.PDC.PRINTER, 'r') as printer_cfg:

            for i, line in enumerate(printer_cfg):
                if saveconfig_line in line:
                    save_lines = True
                    print(f'{name} ✓ SaveConfig Line found in MACHINE PDC Printer File. Saving content...')
                if save_lines:
                    extracted_saveconfig.append(line)

        if (not save_lines):
            print(f'{name} ☓ Printer File found in MACHINE PDC, but no SaveConfig Line. Using SaveConfig Line Default Values.')

    else:
        print(f'{name} ☓ No Printer file found in MACHINE PDC. Using SaveConfig Line Default Values.')

    # CREATE A FILE IN CACHE AND WRITE IT'S LINES BASED ON THE EXTRACTED SAVECONFIG LINE
    try:
        if not os.path.exists(DIR.CACHE.CORE.PDC.PATH):
            os.makedirs(DIR.CACHE.CORE.PDC.PATH)
            print(f'{name} ✓ Created PDC Cache.')
    except Exception as e:
        print(f'{name} ☓ Error trying to create PDC Cache.')
        print(f"{name} {e}")
        exit()
    try:
        with open(DIR.CACHE.CORE.PDC.PRINTER, 'w') as extracted:
            if (save_lines):
                extracted.writelines(extracted_saveconfig)
                print(f'{name} ✓ Successfully extracted SaveConfig Lines from PDC Machine to PDC Cache.')
            else:
                extracted.writelines(saveconfig_backup)
                print(f'{name} ✓ Used Default Values to write the contents of SaveConfig.')
    except Exception as e:
        print(f'{name} ☓ Error trying to open/create the Printer File in PDC Cache.')
        print(f"{name} {e}")
        exit()

    # COPY BOTH SWIERVISION.CONF AND VARIABLES.CFG TO PDC CACHE
    if os.path.exists(DIR.SYSTEM.PDC.SV):
        shutil.copyfile(DIR.SYSTEM.PDC.SV, DIR.CACHE.CORE.PDC.SV)
        print(f'{name} ✓ SV Machine PDC File copied to PDC Cache.')
    elif os.path.exists(DIR.SYSTEM.PDC.BACKUPS.SV):
        print(f'{name} ☓ SV Machine PDC Not found.')
        shutil.copyfile(DIR.SYSTEM.PDC.BACKUPS.SV, DIR.CACHE.CORE.PDC.SV)
        print(f'{name} ✓ SV Machine PDC (Backup) File copied to PDC Cache.')
    elif os.path.exists(DIR.STORE.FRESH.PDC.BACKUPS.SV):
        print(f'{name} ☓ SV Machine PDC (Backup) Not found.')
        shutil.copyfile(DIR.STORE.FRESH.PDC.BACKUPS.SV, DIR.CACHE.CORE.PDC.SV)
        print(f'{name} ✓ SV Fresh PDC (Backup) File copied to PDC Cache.')
    else:
        print(f'{name} ☓ No SV Backup file found at all.')
        exit()

    if os.path.exists(DIR.SYSTEM.PDC.VARIABLES):
        shutil.copyfile(DIR.SYSTEM.PDC.VARIABLES, DIR.CACHE.CORE.PDC.VARIABLES)
        print(f'{name} ✓ Variables Machine PDC File copied to PDC Cache.')
    elif os.path.exists(DIR.SYSTEM.PDC.BACKUPS.VARIABLES):
        print(f'{name} ☓ Variables Machine PDC Not found.')
        shutil.copyfile(DIR.SYSTEM.PDC.BACKUPS.VARIABLES, DIR.CACHE.CORE.PDC.VARIABLES)
        print(f'{name} ✓ Variables Machine PDC (Backup) File copied to PDC Cache.')
    elif os.path.exists(DIR.STORE.FRESH.PDC.BACKUPS.VARIABLES):
        print(f'{name} ☓ Variables Machine PDC (Backup) Not found.')
        shutil.copyfile(DIR.STORE.FRESH.PDC.BACKUPS.VARIABLES, DIR.CACHE.CORE.PDC.VARIABLES)
        print(f'{name} ✓ Variables Fresh PDC (Backup) File copied to PDC Cache.')
    else:
        print(f'{name} ☓ No Variables Backup file found at all.')
        exit()

    # DELETE ALL CONTENT ON PRINTER_DATA/CONFIG
    if os.path.exists(DIR.SYSTEM.PDC.PATH):
        print(f'{name} ✓ Deleting all content in PDC Machine.')
        shutil.rmtree(DIR.SYSTEM.PDC.PATH)
    else:
        print(f"{name} ☓ PDC Machine not found. This really should't happen... Creating it.")
        try:
            os.makedirs(DIR.SYSTEM.PDC.PATH)
        except Exception as e:
            print(f"{name} ☓ Error trying to create PDC Machine Path, maybe a permission error?")
            print(f"{name} {e}")
            exit()

    # TRANSFER ALL CONTENT FROM PDC_FRESH TO MACHINE
    if os.path.exists(DIR.STORE.FRESH.PDC.PATH):
        shutil.copytree(DIR.STORE.FRESH.PDC.PATH, DIR.SYSTEM.PDC.PATH)
        print(print(f'{name} ✓ Transferred all content from PDC Fresh to PDC Machine.'))
    else:
        print(f'{name} ☓ No Fresh PDC Available.')
        exit()

    # COPY BOTH SWIERVISION.CONF AND VARIABLES.CFG TO PDC MACHINE
    try:
        shutil.copyfile(DIR.CACHE.CORE.PDC.SV, DIR.SYSTEM.PDC.SV)
        shutil.copyfile(DIR.CACHE.CORE.PDC.VARIABLES, DIR.SYSTEM.PDC.VARIABLES)
        print(print(f'{name} ✓ Transferred both SV and Variables Files from PDC Cache to PDC Machine.'))
    except Exception as e:
        print(f"{name} ☓ Error trying to copy files from Cache to PDC Machine.")
        print(f"{name} {e}")
        exit()

    # INSERT MAIN CANBUS UUID INTO PRINTER.CFG
    try:
        config = configparser.ConfigParser()
        config.read(DIR.SYSTEM.PDC.BACKUPS.PRINTER)
        if config.has_section('mcu') and config.has_option('mcu', 'canbus_uuid'):
            with open(DIR.CORE.INFO, 'r') as prop_file:
                data = yaml.safe_load(prop_file)
                config.set('mcu', 'canbus_uuid', data['main_canbus_uuid'])
                with open (DIR.SYSTEM.PDC.BACKUPS.PRINTER, 'w') as printercfg_file:
                    config.write(printercfg_file)
                    print(print(f'{name} ✓ PDC Machine Backup Printer file now has updated Canbus UUID (main mcu).'))
    except Exception as e:
        print(print(f'{name} ☓ Error trying to update Canbus UUID in printer cfg file.'))

    # INSERT RP2040 (ONE) CANBUS UUID INTO PRINTER.CFG
    try:
        config = configparser.ConfigParser()
        config.read(DIR.SYSTEM.PDC.BACKUPS.PRINTER)
        if config.has_section('mcu rp2040') and config.has_option('mcu rp2040', 'canbus_uuid'):
            with open(DIR.CORE.INFO, 'r') as prop_file:
                data = yaml.safe_load(prop_file)
                config.set('mcu rp2040', 'canbus_uuid', data['rp2040_one_uuid'])
                with open (DIR.SYSTEM.PDC.BACKUPS.PRINTER, 'w') as printercfg_file:
                    config.write(printercfg_file)
                    print(print(f'{name} ✓ PDC Machine Backup Printer file now has updated Canbus UUID (RP2040 ONE).'))
    except Exception as e:
        print(print(f'{name} ☓ Error trying to update Canbus UUID in printer cfg file.'))

    # TRANSFORM 'BACKUP' PRINTER.CFG FILE INTO USEFUL FILE
    try:
        shutil.copyfile(DIR.SYSTEM.PDC.BACKUPS.PRINTER, DIR.SYSTEM.PDC.PRINTER)
        print(print(f'{name} ✓ PDC Machine Backup Printer file transformed into normal file.'))
    except Exception as e:
        print(print(f'{name} ☓ Error trying to transform PDC Machine Backup Printer File into normal file.'))
        print(f"{name} {e}")
        exit()

    # APPEND CONTENT TO THAT PRINTER.CFG FILE
    try:
        with open(DIR.SYSTEM.PDC.PRINTER, 'a') as printer_cfg:
            with open(DIR.CACHE.CORE.PDC.PRINTER, 'r') as extracted:
                printer_cfg.write('\n')
                for line in extracted:
                    printer_cfg.write(line)
        print(print(f'{name} ✓ Added SaveConfig content to PDC Machine Printer file.'))
    except Exception as e:
        print(print(f'{name} ☓ Error while trying to append SaveConfig content into PDC Machine Printer File'))
        print(f"{name} {e}")

    # OVERWRITE FILES ON MACHINE PDC
    subprocess.run(['sudo', 'bash', DIR.PDC.TRANSFER], check=True)

    securePermission()