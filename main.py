import pygame
import config
import os
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

try:
    pygame.mixer.init(44100, -16, 2, 2048)
    config.SOUND_ENABLED = True
except:
    config.SOUND_ENABLED = False

if __name__ == "__main__":
    boy = Pypboy('Pip-Boy 3000', config.WIDTH, config.HEIGHT)
    print("RUN")
    boy.run()
