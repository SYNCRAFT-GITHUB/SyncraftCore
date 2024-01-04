from startup.modules.transfer import transfer
from startup.modules.upgrade import upgrade
from startup.modules.restart_services import restart_services
from intro.intro import play_boot_video

# rafaelSwi /*
# Executes all Python functions in sequence when booting the machine.
# If you want to add something, create the function in a separate file,
# import the file, and call the function.

transfer()
upgrade()
restart_services()
play_boot_video()