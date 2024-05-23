from flask import Flask, make_response, jsonify
from dirs import DIR
import subprocess
import os

app = Flask("SyncraftCore")

core = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')

def ok():
    return make_response("Executed", 200)

def error():
    return make_response("Error", 500)

def bash(path):
    if os.path.exists(path):
        subprocess.call(['bash'], path)
        return ok()
    else:
        return error()

######## FIXES
###################################################

@app.route('/fix/camera', methods=['POST'])
def fix_camera():
    p = f"{core}/fixes/camera.sh"
    return bash(path=p)

@app.route('/fix/flash', methods=['POST'])
def fix_flash():
    p = f"{core}/fixes/flash.sh"
    return bash(path=p)

@app.route('/fix/light', methods=['POST'])
def fix_light():
    p = f"{core}/fixes/light.sh"
    return bash(path=p)

@app.route('/fix/mainsail', methods=['POST'])
def fix_mainsail():
    p = f"{core}/fixes/mainsail.sh"
    return bash(path=p)

@app.route('/fix/moonraker', methods=['POST'])
def fix_moonraker():
    p = f"{core}/fixes/moonraker.sh"
    return bash(path=p)

@app.route('/fix/reflash', methods=['POST'])
def fix_reflash():
    p = f"{core}/fixes/reflash.sh"
    return bash(path=p)

######## STATE
###################################################

@app.route('/downgrade/all', methods=['POST'])
def downgrade_all():
    p = f"{core}/state/downgrade/apply.sh"
    return bash(path=p)

@app.route('/upgrade/all', methods=['POST'])
def upgrade_all():
    p = f"{core}/state/upgrade/apply.sh"
    return bash(path=p)

######## USB
###################################################

@app.route('/usb/slicer', methods=['POST'])
def usb_slicer():
    p = f"{core}/usb/slicer/transfer.sh"
    return bash(path=p)

@app.route('/usb/logs', methods=['POST'])
def usb_logs():
    p = f"{core}/usb/export_logs.sh"
    return bash(path=p)

@app.route('/usb/update', methods=['POST'])
def usb_update():
    p = f"{core}/usb/update.sh"
    return bash(path=p)

if __name__ == '__main__':
    app.run()