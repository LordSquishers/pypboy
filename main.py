import pygame
import config
import os
import confuse
if config.gpioAvailable():
    import RPi.GPIO as GPIO

if config.gpioAvailable():
    GPIO.setmode(GPIO.BCM)

    # Init framebuffer/touchscreen environment variables
    os.putenv('SDL_VIDEODRIVER', 'fbcon')
    os.putenv('SDL_FBDEV', '/dev/fb1')
#    os.putenv('SDL_MOUSEDRV', 'TSLIB')
#    os.putenv('SDL_MOUSEDEV', '/dev/input/event2')
else:
    print("GPIO UNAVAILABLE")

from pypboy.core import Pypboy

if __name__ == "__main__":
    if config.config['audio']['enabled'].get():
        try:
            pygame.mixer.init(44100, -16, 2, 2048)
        except:
            config.config['audio']['enabled'] = False

    boy = Pypboy('Pip-Boy 3000')
    boy.run()
