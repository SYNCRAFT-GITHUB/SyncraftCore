from startup.modules.transfer import transfer
from startup.modules.upgrade import upgrade
from startup.modules.restart_services import restart_services

transfer()
upgrade()
restart_services()