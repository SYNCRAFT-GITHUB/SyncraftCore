import os

core = os.path.join('/home', 'pi', 'SyncraftCore')

class PATH:
    CORE = core
    INTRO = os.path.join(core, 'intro')
    class FILE:
        KS = os.path.join('/home', 'pi', 'printer_data', 'config', 'KlipperScreen.conf')
    class VIDEO:
        DEFAULT = os.path.join(core, 'intro', 'default.mp4')
        COLORFUL = os.path.join(core, 'intro', 'colorful.mp4')
        INVADER = os.path.join(core, 'intro', 'invader.mp4')

try:

    with open(PATH.FILE.KS, 'r') as config:
        content = ''.join(config.readlines()).lower()
        if 'invader' in content and os.path.exists(PATH.VIDEO.INVADER):
            os.system(f'sudo -u pi cvlc -f --no-video-title-show {PATH.VIDEO.INVADER}')
        if 'colorful' in content and os.path.exists(PATH.VIDEO.COLORFUL):
            os.system(f'sudo -u pi cvlc -f --no-video-title-show {PATH.VIDEO.COLORFUL}')
        elif os.path.exists(PATH.VIDEO.DEFAULT):
            os.system(f'sudo -u pi cvlc -f --no-video-title-show {PATH.VIDEO.DEFAULT}')
        else:
            pass

except Exception as e:
    print (f'[INTRO SCRIPT] Error: {e}')