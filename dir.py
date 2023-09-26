import os

pi = os.path.join('/home', 'pi')
core = os.path.join(pi, 'SyncraftCore')
py = 'apply.py'
sh = 'apply.sh'


class PATH:
    class STORE:
        PATH = os.path.join(core, 'store')
        STOCK = os.path.join(core, 'store', 'stock')
        FRESH = os.path.join(core, 'store', 'fresh')
        KIAUH = os.path.join(core, 'store', 'kiauh')

    class STARTUP:
        PATH = os.path.join(core, 'startup')

    class MACHINE:
        PATH = os.path.join(core, 'machine')
        APPLY = os.path.join(core, 'machine', sh)

    class USB:
        PATH = os.path.join(core, 'usb')

        class LOGS:
            PATH = os.path.join(core, 'usb', 'logs')
            APPLY = os.path.join(core, 'usb', 'logs', sh)

        class UPDATE:
            PATH = os.path.join(core, 'usb', 'update')
            APPLY = os.path.join(core, 'usb', 'update', sh)

    class CACHE:
        PATH = os.path.join(core, 'cache')
        CORE = os.path.join(core, 'cache', 'core')
        PDC = os.path.join(core, 'cache', 'pdc')

    class CHECK:
        PATH = os.path.join(core, 'check')

        class REPO:
            PATH = os.path.join(core, 'check', 'repo')
            APPLY = os.path.join(core, 'check', 'repo', sh)

        class STORAGE:
            PATH = os.path.join(core, 'check', 'storage')
            APPLY = os.path.join(core, 'check', 'storage', py)

        class PDC:
            PATH = os.path.join(core, 'check', 'storage')
            APPLY = os.path.join(core, 'check', 'storage', py)

    class STATE:
        PATH = os.path.join(core, 'state')

        class UPGRADE:
            KS = os.path.join(core, 'state', 'upgrade', 'ks', sh)
            KLE = os.path.join(core, 'state', 'upgrade', 'kle', sh)
            MAINSAIL = os.path.join(core, 'state', 'upgrade', 'mainsail', sh)

        class DOWNGRADE:
            KS = os.path.join(core, 'state', 'downgrade', 'ks', sh)
            KLE = os.path.join(core, 'state', 'downgrade', 'kle', sh)
            MAINSAIL = os.path.join(core, 'state', 'downgrade', 'mainsail', sh)

    class CORE:
        PATH = os.path.join(core, 'core')
        UPDATE = os.path.join(core, 'core', 'update', py)
        CREATE = os.path.join(core, 'core', 'create', py)

    class PDC:
        PATH = os.path.join(core, 'pdc')
        MOONRAKER_CONF = PATH = os.path.join(core, 'pdc', 'moonraker.conf')
