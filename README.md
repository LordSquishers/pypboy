pypboy
======

Bringing the Pipboy-3000 project back to 2024! <br>
Uses a Python/Pygame interface, emulating that of the Pipboy-3000. Uses OpenStreetMap for map data and has been tailored to respond to physical switches over Raspberry Pi's GPIO. Now has custom radio stations!

## Hardware
Follows the original guide by Adafruit (https://learn.adafruit.com/raspberry-pi-pipboy-3000/overview). Uses a generic 3.5" TFT display.

## Installation
First, install RasPiOS 32-bit (Bullseye, desktop) [version used: 2024-10-22-raspios-bullseye-armhf].

Set the username to `pipboy`, and choose your own password (if you choose a different username, you'll need to amend `USER_DIR` and `RADIO_DIR` in `config.py`).

Then, open a terminal and run `sudo raspi-config`.
- Set the WiFi, hostname, timezone, and keyboard layout.
- Enable ssh, SPI, and remote GPIO (optional).

For completeness' sake, run `sudo apt-get update`.

You'll then need to set up a virtual environment. This distribution of Bullseye has python3-venv already installed, but you may need to install it if you aren't using the same version!
You can set the environment in the home directory using `python -m venv env --system-site-packages`.

This project uses GPIOZero and lgpio. To instal the lgpio libraries, run the following:
```sh
cd Documents/
https://abyz.me.uk/lg/download.html
sudo apt install swig python3-dev
sudo apt install python3-setuptools
wget http://abyz.me.uk/lg/lg.zip
unzip lg.zip
cd lg
make
sudo make install
```

Since a generic 3.5" TFT is used (driver is ILI9486), we'll need to install LCD-show. While in `Documents/`, run:
```sh
git clone https://github.com/goodtft/LCD-show.git
chmod -R 755 LCD-show
cd LCD-show
sudo ./LCD35-show
cd ../
```

If you need to rotate the display you can do so by running `sudo ./LCD-show/rotate.sh <0/90/180/270>`.

Finally, to install this program, run `git clone https://github.com/LordSquishers/pypboy.git` and copy the startup script to the desktop 
using `cp pypboy/pipboy.sh ~/Desktop/`. You'll also need to create a directory called `radio` for radio files (`.ogg`) in `Documents/`(can just use `mkdir radio`). A few stations are configured, but they will not have folders or music on a fresh install.

To set the program to automatically run on startup, run `sudo nano /etc/xdg/lxsession/LXDE-pi/autostart` and add `@bash /home/pipboy/Desktop/pipboy.sh` to the end of the file. You may need to give the file executable permissions with `chmod a+x ~/Desktop/pipboy.sh`. Run and enjoy!
## Authors
- grieve, the original author!
- sabas1080, who extended the project and included TFT displays (this version used by Adafruit).
- amolloy, who upgraded the project to Python3 and did significant work to upgrade the code structure :) (Thank you!!!).
- LordSquishers, who is now using the project.
