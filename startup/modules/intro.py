from datetime import datetime
from dirs import DIR
import os

def play_boot_video():

    def play_video(path: str) -> str:
        return os.system(f"sudo -u pi cvlc -f --no-video-title-show {path} 2> /dev/null")

    try:

        current_date = datetime.now().date()

        with open(DIR.SYSTEM.PDC.SV, 'r') as config:
            content = ''.join(config.readlines()).lower()

            if current_date.month == 9 and current_date.day == 17:
                play_video(DIR.INTRO.STAR)
                return None

            if 'invader' in content and os.path.exists(DIR.INTRO.INVADER):
                return play_video(DIR.INTRO.INVADER)
            elif 'colorful' in content and os.path.exists(DIR.INTRO.COLORFUL):
                return play_video(DIR.INTRO.COLORFUL)
            elif 'neon' in content and os.path.exists(DIR.INTRO.DEFAULT):
                return play_video(DIR.INTRO.DEFAULT)
            elif 'evening' in content and os.path.exists(DIR.INTRO.DEFAULT):
                return play_video(DIR.INTRO.DEFAULT)
            elif os.path.exists(DIR.INTRO.DEFAULT):
                return play_video(DIR.INTRO.DEFAULT)
            else:
                pass

    except Exception as e:
        print (f'[INTRO SCRIPT] Error: {e}')