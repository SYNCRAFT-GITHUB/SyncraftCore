from startup.modules.transfer import transfer
from startup.modules.upgrade import upgrade
from startup.modules.restart_services import restart_services
from intro.intro import play_boot_video

transfer()
upgrade()
restart_services()
play_boot_video()