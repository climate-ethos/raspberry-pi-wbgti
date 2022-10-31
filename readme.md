# raspberry-pi-wbgti

This project aims to take a raspberry pi, combined with some external temperature probes to create a GUI for a wbgt index sensor.

## Installation/Setup

RPI = Raspberry Pi

1. Plug noobs OS SD card into the RPI
2. Wire up waveshare 5in screen to RPI
3. Plug in usb C power cable to RPI and select install on Raspberry Pi OS
4. Boot into recovery mode using shift when the RPI turns on
5. Press e to edit the config
6. Comment out the following lines:\
`#camera_auto_detect=1`\
`#dtoverlay=vc4-kms-v3d`
7. Add the following lines under [all]\
`dtoverlay=vc4-fkms-v3d`\
`start_x=1`\
`dtoverlay=w1-gpio`
8. Escape and restart the RPI
9. Wire up the temperature sensors
10. Open a terminal window in the pi and run the following commands:\
`cd`\
`git clone https://github.com/griffith-ethos/raspberry-pi-wbgti.git`\
`cd raspberry-pi-wbgti`
11. Run the temperature sensor program `sudo python digital-probe-temperature.py`
