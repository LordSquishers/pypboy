import pypboy
import config
import numpy
import game
import copy
import traceback
import pygame
import math
from pypboy import data

class Oscilloscope(game.Entity):

    def __init__(self, *args, **kwargs):
        self.WIDTH, self.HEIGHT = 210, 200
        self.TRACE, self.AFTER, self.GREY = (80, 255, 100),(20, 155, 40),(20, 110, 30)
        super(Oscilloscope, self).__init__((self.WIDTH, self.HEIGHT))
        self.rect[0] = 250
        self.rect[1] = 55

        # Create a blank chart with vertical ticks, etc
        self.blank = numpy.zeros((self.WIDTH, self.HEIGHT, 3))
        # Draw x-axis
        self.xaxis = self.HEIGHT // 2
        self.blank[::, self.xaxis] = self.GREY
        self.blank[::, self.HEIGHT - 2] = self.TRACE
        self.blank[::, self.HEIGHT - 1] = self.TRACE
        self.blank[::50, self.HEIGHT - 4] = self.TRACE
        self.blank[::50, self.HEIGHT - 3] = self.TRACE
        self.blank[self.WIDTH - 2, ::] = self.TRACE
        self.blank[self.WIDTH - 1, ::] = self.TRACE
        self.blank[self.WIDTH - 3, ::40] = self.TRACE
        self.blank[self.WIDTH - 4, ::40] = self.TRACE

        # Draw vertical ticks
        vticks = [-80, -40, +40, +80]
        for vtick in vticks: self.blank[::5, self.xaxis + vtick] = self.GREY # Horizontals
        for vtick in vticks: self.blank[::50, ::5] = self.GREY			   # Verticals

        self.song_data = False

    def set_song(self, filename):
        self.song_data = data.LogSpectrum(filename) 
        return

    def update(self, *args, **kwargs):
        try:
            pixels = copy.copy(self.blank)

            if self.song_data:
                start = pygame.mixer.music.get_pos() / 1000.0
                time = start * 50.0

                _, lpower = self.song_data.get_left(start-0.001, start+0.001)
                _, rpower = self.song_data.get_right(start-0.001, start+0.001)
                power = (lpower + rpower) / 2.0

                offset = 1
                for x in range(self.WIDTH):
                    offset = offset - 1
                    if offset < -1:
                        offset = offset + 1.1		 
                    try:
                        pow = power[int(x/10)]
                        log = math.log10( pow )
                        offset = ((pow / math.pow(10, math.floor(log))) + log) * 1.8
                    except:
                        pass
                    try: 
#                        y = int(float(self.xaxis) - (math.sin((float(x)+float(time))/5.0)*2.0*offset))
                        y = int(float(self.xaxis) + offset * 2.0)
                        pixels[x][y] = self.TRACE
                        pixels[x][y-1] = self.AFTER
                        pixels[x][y+1] = self.AFTER
                        if abs(y) > 120:
                            pixels[x][y-2] = self.AFTER
                            pixels[x][y+2] = self.AFTER
                    except Exception as e:
                        print(traceback.format_exc())

            pygame.surfarray.blit_array(self.image, pixels)	 # Blit the screen buffer
        except:
            print(traceback.format_exc())
