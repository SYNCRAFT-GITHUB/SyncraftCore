import os

syncraftcore_dir = os.path.dirname(__file__)

class DIR:
    PATH = syncraftcore_dir
    class SYSTEM:
        class PDC:
            PATH = os.path.join(os.path.dirname(__file__), '..', 'printer_data', 'config')
            KS = os.path.join(os.path.dirname(__file__), '..', 'printer_data', 'config', 'KlipperScreen.conf')
            PRINTER = os.path.join(os.path.dirname(__file__), '..', 'printer_data', 'config', 'printer.cfg')
            VARIABLES = os.path.join(os.path.dirname(__file__), '..', 'printer_data', 'config', 'variables.cfg')
            class BACKUPS:
                PATH = os.path.join(os.path.dirname(__file__), '..', 'printer_data', 'config', 'backups')
                KS = os.path.join(os.path.dirname(__file__), '..', 'printer_data', 'config', 'backups', 'KlipperScreen.conf')
                PRINTER = os.path.join(os.path.dirname(__file__), '..', 'printer_data', 'config', 'backups', 'printer.cfg')
                VARIABLES = os.path.join(os.path.dirname(__file__), '..', 'printer_data', 'config', 'backups', 'variables.cfg')
        class MOONRAKER:
            PATH = os.path.join(os.path.dirname(__file__), '..', 'moonraker')
        class KLIPPER:
            PATH = os.path.join(os.path.dirname(__file__), '..', 'klipper')
        class MAINSAIL:
            PATH = os.path.join(os.path.dirname(__file__), '..', 'mainsail')
        class KS:
            PATH = os.path.join(os.path.dirname(__file__), '..', 'KlipperScreen')
    class CORE:
        PATH = os.path.join(syncraftcore_dir, 'core')
        CREATE = os.path.join(syncraftcore_dir, 'core', 'create.py')
        INFO = os.path.join(syncraftcore_dir, 'core', 'info.yaml')
        REQUIREMENTS = os.path.join(syncraftcore_dir, 'core', 'requirements.txt')
        SET_CANBUS_UUID = os.path.join(syncraftcore_dir, 'core', 'set_canbus_uuid.py')
        UPDATE = os.path.join(syncraftcore_dir, 'core', 'update.py')
    class CACHE:
        PATH = os.path.join(syncraftcore_dir, 'cache')
        class CORE:
            PATH = os.path.join(syncraftcore_dir, 'cache', 'core')
            class KLE:
                PATH = os.path.join(syncraftcore_dir, 'cache', 'core', 'klipper-led_effect')
            class KLIPPER:
                PATH = os.path.join(syncraftcore_dir, 'cache', 'core', 'klipper')
            class MOONRAKER:
                PATH = os.path.join(syncraftcore_dir, 'cache', 'core', 'moonraker')
            class MAINSAIL:
                PATH = os.path.join(syncraftcore_dir, 'cache', 'core', 'mainsail')
        class KS:
            PATH = os.path.join(syncraftcore_dir, 'cache', 'core', 'KlipperScreenIDEX')
        class PDC:
            PATH = os.path.join(syncraftcore_dir, 'cache', 'core', 'IDEXConfig')
            KS = os.path.join(syncraftcore_dir, 'cache', 'core', 'IDEXConfig', 'KlipperScreen.conf')
            PRINTER = os.path.join(syncraftcore_dir, 'cache', 'core', 'IDEXConfig', 'printer.cfg')
            VARIABLES = os.path.join(syncraftcore_dir, 'cache', 'core', 'IDEXConfig', 'variables.cfg')
            class BACKUPS:
                PATH = os.path.join(syncraftcore_dir, 'cache', 'core', 'IDEXConfig', 'backups')
                KS = os.path.join(syncraftcore_dir, 'cache', 'core', 'IDEXConfig', 'backups', 'KlipperScreen.conf')
                PRINTER = os.path.join(syncraftcore_dir, 'cache', 'core', 'IDEXConfig', 'backups', 'printer.cfg')
                VARIABLES = os.path.join(syncraftcore_dir, 'cache', 'core', 'IDEXConfig', 'backups', 'variables.cfg')
    class BACKUPS:
        PATH = os.path.join(syncraftcore_dir, 'backups')
    class ENV:
        PATH = os.path.join(syncraftcore_dir, 'env')
    class INTRO:
        PATH = os.path.join(syncraftcore_dir, 'intro')
        DEFAULT = os.path.join(syncraftcore_dir, 'intro', 'default.mp4')
        COLORFUL = os.path.join(syncraftcore_dir, 'intro', 'colorful.mp4')
        INVADER = os.path.join(syncraftcore_dir, 'intro', 'invader.mp4')
        INTRO = os.path.join(syncraftcore_dir, 'intro', 'intro.py')
    class MACHINE:
        PATH = os.path.join(syncraftcore_dir, 'machine')
        APPLY = os.path.join(syncraftcore_dir, 'machine', 'apply.sh')
        class BOOTCMDLINE:
            PATH = os.path.join(syncraftcore_dir, 'machine', 'bootcmdline')
            APPLY = os.path.join(syncraftcore_dir, 'machine', 'bootcmdline', 'apply.sh')
        class PACKAGES:
            PATH = os.path.join(syncraftcore_dir, 'machine', 'packages')
            APPLY = os.path.join(syncraftcore_dir, 'machine', 'packages', 'apply.sh')
        class PYTHONREQ:
            PATH = os.path.join(syncraftcore_dir, 'machine', 'pythonreq')
            APPLY = os.path.join(syncraftcore_dir, 'machine', 'pythonreq', 'apply.sh')
        class RCLOCAL:
            PATH = os.path.join(syncraftcore_dir, 'machine', 'rclocal')
            APPLY = os.path.join(syncraftcore_dir, 'machine', 'rclocal', 'apply.sh')
        class UDISKRULES:
            PATH = os.path.join(syncraftcore_dir, 'machine', 'udiskrules')
            APPLY = os.path.join(syncraftcore_dir, 'machine', 'udiskrules', 'apply.sh')
        class USBSXSERVICE:
            PATH = os.path.join(syncraftcore_dir, 'machine', 'usbsxservice')
            APPLY = os.path.join(syncraftcore_dir, 'machine', 'usbsxservice', 'apply.sh')
        class XWRAPPER:
            PATH = os.path.join(syncraftcore_dir, 'machine', 'xwrapper')
            APPLY = os.path.join(syncraftcore_dir, 'machine', 'xwrapper', 'apply.sh')
    class MATERIALS:
        PATH = os.path.join(syncraftcore_dir, 'materials')
        STOCK = os.path.join(syncraftcore_dir, 'materials', 'stock.json')
        CUSTOM = os.path.join(syncraftcore_dir, 'materials', 'custom.json')
    class PDC:
        PATH = os.path.join(syncraftcore_dir, 'pdc')
        TRANSFER = os.path.join(syncraftcore_dir, 'pdc', 'transfer.sh')
    class STARTUP:
        PATH = os.path.join(syncraftcore_dir, 'startup')
        def GET_FROM_TERM(term) -> str:
            content = os.listdir(os.path.join(syncraftcore_dir, 'startup'))
            for item in content:
                if term.lower() in item.lower():
                    return os.path.join(syncraftcore_dir, 'startup', item)
    class STATE:
        PATH = os.path.join(syncraftcore_dir, 'state')
        class DOWNGRADE:
            PATH = os.path.join(syncraftcore_dir, 'state', 'downgrade')
            APPLY = os.path.join(syncraftcore_dir, 'state', 'downgrade', 'apply.sh')
            class KLE:
                PATH = os.path.join(syncraftcore_dir, 'state', 'downgrade', 'kle')
                APPLY = os.path.join(syncraftcore_dir, 'state', 'downgrade', 'kle', 'apply.sh')
            class KS:
                PATH = os.path.join(syncraftcore_dir, 'state', 'downgrade', 'ks')
                APPLY = os.path.join(syncraftcore_dir, 'state', 'downgrade', 'ks', 'apply.sh')
            class MAINSAIL:
                PATH = os.path.join(syncraftcore_dir, 'state', 'downgrade', 'mainsail')
                APPLY = os.path.join(syncraftcore_dir, 'state', 'downgrade', 'mainsail', 'apply.sh')
        class UPGRADE:
            PATH = os.path.join(syncraftcore_dir, 'state', 'upgrade')
            APPLY = os.path.join(syncraftcore_dir, 'state', 'upgrade', 'apply.sh')
            class KLE:
                PATH = os.path.join(syncraftcore_dir, 'state', 'upgrade', 'kle')
                APPLY = os.path.join(syncraftcore_dir, 'state', 'upgrade', 'kle', 'apply.sh')
            class KS:
                PATH = os.path.join(syncraftcore_dir, 'state', 'upgrade', 'ks')
                APPLY = os.path.join(syncraftcore_dir, 'state', 'upgrade', 'ks', 'apply.sh')
            class MAINSAIL:
                PATH = os.path.join(syncraftcore_dir, 'state', 'upgrade', 'mainsail')
                APPLY = os.path.join(syncraftcore_dir, 'state', 'upgrade', 'mainsail', 'apply.sh')
    class STORE:
        PATH = os.path.join(syncraftcore_dir, 'store')
        class KIAUH:
            PATH = os.path.join(syncraftcore_dir, 'store', 'kiauh')
        class FRESH:
            PATH = os.path.join(syncraftcore_dir, 'store', 'fresh')
            class KLE:
                PATH = os.path.join(syncraftcore_dir, 'store', 'fresh', 'klipper-led_effect')
            class KLIPPER:
                PATH = os.path.join(syncraftcore_dir, 'store', 'fresh', 'klipper')
            class MOONRAKER:
                PATH = os.path.join(syncraftcore_dir, 'store', 'fresh', 'moonraker')
            class MAINSAIL:
                PATH = os.path.join(syncraftcore_dir, 'store', 'fresh', 'mainsail')
            class KS:
                PATH = os.path.join(syncraftcore_dir, 'store', 'fresh', 'KlipperScreenIDEX')
            class PDC:
                PATH = os.path.join(syncraftcore_dir, 'store', 'fresh', 'IDEXConfig')
                KS = os.path.join(syncraftcore_dir, 'store', 'fresh', 'IDEXConfig', 'KlipperScreen.conf')
                PRINTER = os.path.join(syncraftcore_dir, 'store', 'fresh', 'IDEXConfig', 'printer.cfg')
                VARIABLES = os.path.join(syncraftcore_dir, 'store', 'fresh', 'IDEXConfig', 'variables.cfg')
                class BACKUPS:
                    PATH = os.path.join(syncraftcore_dir, 'store', 'fresh', 'IDEXConfig', 'backups')
                    KS = os.path.join(syncraftcore_dir, 'store', 'fresh', 'IDEXConfig', 'backups', 'KlipperScreen.conf')
                    PRINTER = os.path.join(syncraftcore_dir, 'store', 'fresh', 'IDEXConfig', 'backups', 'printer.cfg')
                    VARIABLES = os.path.join(syncraftcore_dir, 'store', 'fresh', 'IDEXConfig', 'backups', 'variables.cfg')
        class STOCK:
            PATH = os.path.join(syncraftcore_dir, 'store', 'stock')
            class KLE:
                PATH = os.path.join(syncraftcore_dir, 'store', 'stock', 'klipper-led_effect')
            class KLIPPER:
                PATH = os.path.join(syncraftcore_dir, 'store', 'stock', 'klipper')
            class MOONRAKER:
                PATH = os.path.join(syncraftcore_dir, 'store', 'stock', 'moonraker')
            class MAINSAIL:
                PATH = os.path.join(syncraftcore_dir, 'store', 'stock', 'mainsail')
            class KS:
                PATH = os.path.join(syncraftcore_dir, 'store', 'stock', 'KlipperScreenIDEX')
            class PDC:
                PATH = os.path.join(syncraftcore_dir, 'store', 'stock', 'IDEXConfig')
                KS = os.path.join(syncraftcore_dir, 'store', 'stock', 'IDEXConfig', 'KlipperScreen.conf')
                PRINTER = os.path.join(syncraftcore_dir, 'store', 'stock', 'IDEXConfig', 'printer.cfg')
                VARIABLES = os.path.join(syncraftcore_dir, 'store', 'stock', 'IDEXConfig', 'variables.cfg')
                class BACKUPS:
                    PATH = os.path.join(syncraftcore_dir, 'store', 'stock', 'IDEXConfig', 'backups')
                    KS = os.path.join(syncraftcore_dir, 'store', 'stock', 'IDEXConfig', 'backups', 'KlipperScreen.conf')
                    PRINTER = os.path.join(syncraftcore_dir, 'store', 'stock', 'IDEXConfig', 'backups', 'printer.cfg')
                    VARIABLES = os.path.join(syncraftcore_dir, 'store', 'stock', 'IDEXConfig', 'backups', 'variables.cfg')
    class USB:
        PATH = os.path.join(syncraftcore_dir, 'usb')
        EXPORT_LOGS = os.path.join(syncraftcore_dir, 'usb', 'export_logs.sh')
        UPDATE = os.path.join(syncraftcore_dir, 'usb', 'update.sh')
        class MATERIALS:
            PATH = os.path.join(syncraftcore_dir, 'usb', 'materials')
            EXPORT = os.path.join(syncraftcore_dir, 'usb', 'materials', 'export.sh')
            IMPORT = os.path.join(syncraftcore_dir, 'usb', 'materials', 'import.sh')
        class SLICER:
            PATH = os.path.join(syncraftcore_dir, 'usb', 'slicer')
            TRANSFER = os.path.join(syncraftcore_dir, 'usb', 'slicer', 'transfer.sh')