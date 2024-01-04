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