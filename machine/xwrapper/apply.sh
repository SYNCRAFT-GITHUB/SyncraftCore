# rafaelSwi /*
# Without this, front-end will not start.
# I don't recommend ever removing or touching this.

xwrapper='allowed_users=anybody
needs_root_rights=yes'

process='Modify Xwrapper Config.'
echo "[HELPER] START: $process."
echo -e "$xwrapper" | sudo tee /etc/X11/Xwrapper.config
sudo chmod +x /etc/X11/Xwrapper.config
echo "[HELPER] DONE: $process."