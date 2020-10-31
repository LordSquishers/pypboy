import pypboy
import config
import numpy
import game
import copy
import traceback
import pygame
import math
import time
import soundfile as sf

class SoundData:
    left = None
    right = None

    def __init__(self, filename):
        a, self.samplerate = sf.read(filename)

        if a.ndim > 1:
            self.stereo = True
            self.left = a[:, 0]
            self.right = a[:, 1]
        else:
            self.stereo = False
            self.left = a
            self.right = []

    def is_stereo(self):
        return self.stereo

    def get_samples(self, data, start, stop):
        """
        Return the raw samples, between start and stop
        time in seconds.
        """
        start = int(start * self.samplerate)
        stop = int(stop * self.samplerate)
        return data[start:stop]

    def get_left(self, start, stop):
        return self.get_samples(self.left, start, stop)

    def get_right(self, start, stop):
        return self.get_samples(self.right, start, stop)

class Oscilloscope(game.Entity):

    def __init__(self, *args, **kwargs):
        self.WIDTH, self.HEIGHT = 210, 200
        self.TRACE, self.AFTER, self.GREY = (80, 255, 100),(20, 155, 40),(20, 110, 30)
        super(Oscilloscope, self).__init__((self.WIDTH, self.HEIGHT))
        self.rect[0] = 250
        self.rect[1] = 55

        self.last_update = 0

        self.width_factor = config.user_config['audio']['oscilloscope_factor'].get()

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
        self.last_start = -1
        self.song_data = SoundData(filename) 

    def update(self, *args, **kwargs):
        start = pygame.mixer.music.get_pos() / 1000.0
        if start == self.last_start:
            return
        self.last_start = start

        try:
            ms = time.time_ns() // 1000000 
            if (ms - self.last_update) > 500:
                self.last_update = ms

                pixels = copy.copy(self.blank)

                if self.song_data:
                    end = start + self.WIDTH * self.width_factor

                    lsamples = self.song_data.get_left(start, end)
                    rsamples = []
                    if self.song_data.is_stereo():
                        rsamples = self.song_data.get_right(start, end)

                    for x in range(self.WIDTH):
                        try: 
                            samp = lsamples[x]
                            if rsamples != []:
                                samp = (samp + rsamples[x]) / 2

                            y = int(float(self.xaxis) + samp * self.HEIGHT * 0.8)
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
