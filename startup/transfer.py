import os
import shutil

script_name: str = ('\033[34m' + '[TRANSFER SCRIPT]' + '\033[0m')
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

def clear_folder(dir):
    try:
        for item in os.listdir(dir):
            item_path = os.path.join(dir, item)

            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)

    except Exception as e:
        print(f"{script_name} ERROR: {e}")

def transfer_files(source_dir, destination_dir, block_list):
    for root, _, files in os.walk(source_dir):
        for file in files:
            src_file = os.path.join(root, file)
            rel_path = os.path.relpath(src_file, source_dir)
            dst_file = os.path.join(destination_dir, rel_path)
            
            if not any(block_name in rel_path.split(os.sep) for block_name in block_list):
                os.makedirs(os.path.dirname(dst_file), exist_ok=True)
                shutil.copy2(src_file, dst_file)
                try:
                    os.chmod(dst_file, 0o777)
                    os.chown(dst_file, 1000, 1000)
                except:
                    pass

def save_config_lines(input_file_path, output_file_path):
    saving = False
    config_lines = []
    times_found = 0

    try:
        with open(input_file_path, 'r') as input_file:
            for line in input_file:
                if times_found <= 1:
                    if saveconfig_line in line:
                        saving = True
                        times_found += 1
                        if times_found <= 1:
                            config_lines.append('\n')
                            config_lines.append(line)
                    elif saving:
                        config_lines.append(line)

        if config_lines:
            with open(output_file_path, 'w') as output_file:
                output_file.writelines(config_lines)
    except:
        with open(output_file_path, 'w') as output_file:
                output_file.writelines(saveconfig_backup)

def append_file_contents(input_file_path, output_file_path):

    with open(output_file_path, 'r') as input_file:
        for line in input_file:
            if saveconfig_line in line:
                print (f"{script_name} \"{saveconfig_line}\" DETECTED IN \"{output_file_path}\".")
                exit()

    try:
    
        with open(input_file_path, 'r') as input_file:
            content_to_append = input_file.read()

        with open(output_file_path, 'a') as output_file:
            output_file.write(content_to_append)

    except:

        with open(output_file_path, 'a') as output_file:
            output_file.write(saveconfig_backup)

def create_printer (pdc_dir):
    backups = os.path.join(pdc_dir, 'backups')
    if not os.path.exists(backups):
        os.mkdir(backups)
    for file in os.listdir(backups):
        if file in ['backup-KlipperScreen.conf', 'backup-printer.cfg', 'backup-variables.cfg']:
            file_to_copy = os.path.join(backups, file)
            file_to_paste = os.path.join(pdc_dir, file.replace('backup-', '', 1))
            shutil.copyfile(file_to_copy, file_to_paste)

if __name__ == "__main__":

    class DIR:
        CORE = os.path.join('/home', 'pi', 'SyncraftCore')
        PDC_FRESH = os.path.join('/home', 'pi', 'SyncraftCore', 'softwares', 'printerdataconfig')
        PDC_STOCK = os.path.join('/home', 'pi', 'SyncraftCore', 'stock', 'printerdataconfig')
        PDC_MACHINE = os.path.join('/home', 'pi', 'printer_data', 'config')
        CONFIG_FILE = os.path.join('/home', 'pi', 'printer_data', 'config', 'printer.cfg')
        SAVECONFIG_FILE = os.path.join('/home', 'pi', 'SyncraftCore', 'cache', 'pdc', 'saveconfig.cfg')
        CACHE = os.path.join('/home', 'pi', 'SyncraftCore', 'cache', 'pdc')
        CACHE_CONFIG_FILE = os.path.join('/home', 'pi', 'SyncraftCore', 'cache', 'pdc', 'printer.cfg')

    ############################################################################
    ###### INSERT IN THE ARRAY WHAT SHOULD BE BLOCKED DURING THE TRANSFER ######
    ############################################################################
    ###### * Files must have the extension                                ######
    ###### * Folders can be referenced                                    ######
    ###### * Subfolders cannot be referenced                              ######
    ############################################################################

    # If you want to become a caveman and skip updates, change this variable to True
    caveman = False

    # Array that blocks specific names
    block = ["KlipperScreen.conf", "variables.cfg"]

    if not caveman:

        clear_folder(DIR.CACHE)
        save_config_lines(DIR.CONFIG_FILE, DIR.SAVECONFIG_FILE)
        transfer_files(DIR.PDC_FRESH, DIR.CACHE, block_list=[])
        create_printer(DIR.CACHE)
        append_file_contents(DIR.SAVECONFIG_FILE, DIR.CACHE_CONFIG_FILE)
        transfer_files(DIR.CACHE, DIR.PDC_MACHINE, block_list=block)

    print(f"{script_name} DONE.")
