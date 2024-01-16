import os

def restart_services():
    try:
        os.system('sudo service klipper restart')
        os.system('sudo systemctl daemon-reload')
        os.system('service systemd-udevd --full-restart')
        os.system('sudo service sxusb restart')
        os.system('sudo service SwierVision restart &')
    except:
        pass