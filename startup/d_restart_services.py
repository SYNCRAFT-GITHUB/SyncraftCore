import os

try:
    os.system('sudo service klipper restart')
    os.system('sudo systemctl daemon-reload')
    os.system('service systemd-udevd --full-restart')
    os.system('sudo service sxusb restart')
except:
    pass