# rafaelSwi /*
# The purpose of this is to make the machine to boot fast and clean.
# For some reason, even using “loglevel=1” the terminal continues to appear, and i don't know why.
# I want to avoid setting the terminal to black as that would fix but would be very stupid.

path=/boot/cmdline.txt
content="consoleblank=1 logo.nologo quiet loglevel=1 plymouth.enable=0 vt.global_cursor_default=0 plymouth.ignore-serial-consoles splash fastboot noatime nodiratime noram"

process='Modify CMDLINE.'
echo "[HELPER] START: $process."
if grep -q "rootwait" "$path"; then
    clean=$(grep "rootwait" "$path" | sed 's/\(rootwait\).*$/\1/')
    echo -e "$clean $content" | sudo tee /boot/cmdline.txt
    sudo chmod +x /boot/cmdline.txt
    echo "[HELPER] DONE: $process."
else
    echo "[HELPER] ERROR: $process."
fi