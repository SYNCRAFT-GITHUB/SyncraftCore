import os
import shutil

saveconfig_line: str = '#*# <---------------------- SAVE_CONFIG ---------------------->'
saveconfig_backup: str = """
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
    PDC_FRESH = os.path.join(core, 'store', 'fresh', 'printerdataconfig')
    PDC_MACHINE = pdc
    PDC_CACHE = os.path.join(core, 'cache', 'pdc')
    class FILE:
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
    MACHINE_HAS_LINE = False

extracted_saveconfig = []

# TRY TO FIND THE SAVECONFIG LINE IN PRINTER.CFG
with open(PATH.FILE.MACHINE.PRINTER, 'r') as printer_cfg:

    for i, line in enumerate(printer_cfg):
        if saveconfig_line in line:
            BOOL.SAVE_LINES = True
        if BOOL.SAVE_LINES:
            extracted_saveconfig.append(line)

# CREATE A FILE IN CACHE AND WRITE IT'S LINES BASED ON THE EXTRACTED SAVECONFIG LINE
with open(PATH.FILE.CACHE.PRINTER, 'w') as extracted:

    extracted.writelines(extracted_saveconfig)

# COPY BOTH KLIPPERSCREEN.CONF AND VARIABLES.CFG TO PDC CACHE
shutil.copyfile(PATH.FILE.MACHINE.KS, PATH.FILE.CACHE.KS)
shutil.copyfile(PATH.FILE.MACHINE.VARIABLES, PATH.FILE.CACHE.VARIABLES)

# DELETE ALL CONTENT ON PRINTER_DATA/CONFIG
shutil.rmtree(PATH.PDC_MACHINE)

# TRANSFER ALL CONTENT FROM PDC_FRESH TO MACHINE
shutil.copytree(PATH.PDC_FRESH, PATH.PDC_MACHINE)

# COPY BOTH KLIPPERSCREEN.CONF AND VARIABLES.CFG TO PDC MACHINE
shutil.copyfile(PATH.FILE.CACHE.KS, PATH.FILE.MACHINE.KS)
shutil.copyfile(PATH.FILE.CACHE.VARIABLES, PATH.FILE.MACHINE.VARIABLES)

# TRANSFORM 'BACKUP' PRINTER.CFG FILE INTO USEFUL FILE
shutil.copyfile(PATH.FILE.PDC_BACKUP.PRINTER, PATH.FILE.MACHINE.PRINTER)

# APPEND CONTENT TO THAT PRINTER.CFG FILE
with open(PATH.FILE.MACHINE.PRINTER, 'a') as printer_cfg:
    with open(PATH.FILE.CACHE.PRINTER, 'r') as extracted:
        printer_cfg.write('\n')
        for line in extracted:
            printer_cfg.write(line)

# MAKE SURE THAT USER 'pi' OWNS THE MACHINE PATH
os.chown(PATH.PDC_MACHINE, 1000, 1000)