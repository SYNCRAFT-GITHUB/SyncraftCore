from datetime import datetime
from dirs import DIR
import os

def play_boot_video():

    try:

        current_date = datetime.now().date()

        with open(DIR.SYSTEM.PDC.KS, 'r') as config:
            content = ''.join(config.readlines()).lower()

            if current_date.month == 12 and current_date.day == 15:
                os.system(f'sudo -u pi cvlc -f --no-video-title-show {DIR.INTRO.STAR}')
                return None

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