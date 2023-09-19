import os
import shutil

home = os.path.expanduser("~")

printerdata_dir = os.path.join(home, "printer_data")
machine_dir = os.path.join(printerdata_dir, "config")
pdc_dir = os.path.join(home, "SyncraftCore", "stock")
new_pdc_dir = os.path.join(printerdata_dir, "printerdataconfig")

if os.path.exists(machine_dir):
    shutil.rmtree(machine_dir)

if os.path.exists(new_pdc_dir):
    shutil.rmtree(new_pdc_dir)

for item in os.listdir(pdc_dir):
    source_item = os.path.join(pdc_dir, item)
    destination_item = os.path.join(printerdata_dir, item)

    if os.path.isdir(source_item):
        shutil.copytree(source_item, destination_item)
    else:
        shutil.copy2(source_item, destination_item)

os.rename(new_pdc_dir, machine_dir)