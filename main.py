import pygame
import config
import os
import confuse
if config.gpioAvailable():
    import gpiozero
    
if config.gpioAvailable():
    driver = config.user_config['video']['driver'].get()
    print("Using driver %s" % driver)
    os.putenv('SDL_VIDEODRIVER', driver)

    fbdev = config.user_config['video']['fbdev'].get()
    os.putenv('SDL_FBDEV', fbdev)
else:
    print("GPIO UNAVAILABLE")

from pypboy.core import Pypboy

if __name__ == "__main__":
    if config.user_config['audio']['enabled'].get():
        print('Audio enabled.');
        try:
            pygame.mixer.init(44100, -16, 2, 2048)
        except Exception as e:
            print('Audio init failed: ', e);
            config.user_config['audio']['enabled'] = False

    boy = Pypboy('Pip-Boy 3000')
    boy.run()
