content="ENV{ID_FS_USAGE}==\"filesystem\", ENV{UDISKS_FILESYSTEM_SHARED}=\"1\""

process='Apply udisks Rules.'
echo "[HELPER] START: $process."
echo $content | sudo tee /etc/udev/rules.d/99-udisks2.rules
echo "[HELPER] DONE: $process."