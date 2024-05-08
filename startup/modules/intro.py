from datetime import datetime
from dirs import DIR
import yaml
import os

# This script plays the Syncraft startup video.
# If you add "intro-preference" in the info.yaml file with the filename,
# it will always play that video. For example, "new.mp4" will always play
# whatever is in intro/new.mp4, if the file exists.

def play_boot_video():

    def play_video(path: str) -> str:
        return os.system(f"sudo -u pi cvlc -f --no-video-title-show {path} 2> /dev/null")

    try:

        with open(DIR.CORE.INFO, 'r') as prop:
            prop = yaml.safe_load(prop)
            preference = prop.get('intro-preference')
            if preference:
                new_video_path = os.path.join(DIR.INTRO.PATH, "preference", preference)
                if os.path.exists(new_video_path):
                    return play_video(new_video_path)

        current_date = datetime.now().date()

        if os.path.exists(DIR.SYSTEM.PDC.SV):
            with open(DIR.SYSTEM.PDC.SV, 'r') as config:
                content = ''.join(config.readlines()).lower()

                if current_date.month == 9 and current_date.day == 17:
                    return play_video(DIR.INTRO.STAR)

                if current_date.month == 12 and current_date.day in [23, 24, 25]:
                    return play_video(DIR.INTRO.SNOW)

                if current_date.month == 1 and current_date.day == 1:
                    return play_video(DIR.INTRO.FIREWORKS)

                if 'invader' in content and os.path.exists(DIR.INTRO.INVADER):
                    return play_video(DIR.INTRO.INVADER)
                elif 'neon' in content and os.path.exists(DIR.INTRO.DEFAULT):
                    return play_video(DIR.INTRO.DEFAULT)
                elif 'evening' in content and os.path.exists(DIR.INTRO.DEFAULT):
                    return play_video(DIR.INTRO.DEFAULT)
                elif os.path.exists(DIR.INTRO.DEFAULT):
                    return play_video(DIR.INTRO.DEFAULT)
                else:
                    pass
        else:
            if os.path.exists(DIR.INTRO.DEFAULT):
                return play_video(DIR.INTRO.DEFAULT)

    except Exception as e:
        print (f'[INTRO SCRIPT] Error: {e}')