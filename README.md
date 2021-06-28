# pi-relay
GPIO relay control for the Raspberry Pi

## Hardware requirements
- A Raspberry Pi (preferably a B model, works best if your board has a header that powers up with 8 pins in the high state)
- A relay board (like the Sainsmart 8 channel relay board)
- Cabling to connect them together

## Software requirements
- Raspberry Pi OS (recommended)
- Python (Pi OS ships with this)
- RPi.GPIO Python module (Pi OS ships with this)
- ncurses Python module (Pi OS ships with this)

## Recommended configuration and installation
- Clone repo
- Launch raspi-config and disable everything using the GPIO pins, then shut down
- Attach the relay board to the Pi and power
- Power up the Pi
- When system is booted, launch a terminal and run script

## NOTES
- Before running the script, check to see if your relay board uses conventional logic or inverted logic.  Adjust the variable provided in the script if necessary.
- Once the script is running, it is not recommended to exit the program or reboot the Pi as this will turn off all outputs or leave them in an unknown state.

## Screenshot
![Screenshot](https://github.com/bunder2015/pi-relay/raw/master/screenshot.png?raw=true)
