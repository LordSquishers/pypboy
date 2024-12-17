#!/bin/bash

# Update to latest version from git
rm -rf /home/pipboy/Documents/pypboy
git clone https://github.com/LordSquishers/pypboy.git /home/pipboy/Documents/pypboy

# Run program
source /home/pipboy/env/bin/activate
python /home/pipboy/Documents/pypboy/main.py