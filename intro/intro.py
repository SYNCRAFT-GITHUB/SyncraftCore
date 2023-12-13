from dirs import DIR
import os

def play_boot_video():

    try:

        with open(DIR.SYSTEM.PDC.KS, 'r') as config:
            content = ''.join(config.readlines()).lower()
            if 'invader' in content and os.path.exists(DIR.INTRO.INVADER):
                os.system(f'sudo -u pi cvlc -f --no-video-title-show {DIR.INTRO.INVADER}')
            if 'colorful' in content and os.path.exists(DIR.INTRO.COLORFUL):
                os.system(f'sudo -u pi cvlc -f --no-video-title-show {DIR.INTRO.COLORFUL}')
            if 'neon' in content and os.path.exists(DIR.INTRO.NEON):
                os.system(f'sudo -u pi cvlc -f --no-video-title-show {DIR.INTRO.NEON}')
            if 'evening' in content and os.path.exists(DIR.INTRO.DEFAULT):
                os.system(f'sudo -u pi cvlc -f --no-video-title-show {DIR.INTRO.DEFAULT}')
            elif os.path.exists(DIR.INTRO.DEFAULT):
                os.system(f'sudo -u pi cvlc -f --no-video-title-show {DIR.INTRO.DEFAULT}')
            else:
                pass

    except Exception as e:
        print (f'[INTRO SCRIPT] Error: {e}')