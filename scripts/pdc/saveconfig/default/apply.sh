content='
#*# <---------------------- SAVE_CONFIG ---------------------->
#*# DO NOT EDIT THIS BLOCK OR BELOW. The contents are auto-generated.
#*#
#*# [probe]
#*# z_offset = -0.360
#*#
#*# [stepper_z]
#*# position_endstop = 342.855
#*#
'

pdc_klipper="/home/pi/printer_data/config"

process='Add saveconfig to printer.cfg File.'
echo "[HELPER] START: $process."
echo "$content" >> "$pdc_klipper/printer.cfg"
echo "[HELPER] DONE: $process."