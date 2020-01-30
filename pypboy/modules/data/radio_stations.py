import os
import config
import game
import pygame
import time
from random import choice

class MusicPlayer:
    def __init__(self, filename):
        self.filename = filename
        self.playing = False
        self.last_pause_pos = 0
        self.last_start = time.time()

    def play(self, start_pos = 0):
        self.playing = True
        self.last_start = time.time()
        pygame.mixer.music.load(self.filename)
        try:
            pygame.mixer.music.play(0, start_pos)
            print(f'Song goes {self.filename}')
        except:
            print(f'Song was over. {self.filename}')
            return False
        return True

    def pause(self):
        self.playing = False
        self.last_pause_pos += time.time() - self.last_start
        pygame.mixer.music.stop()
        print(f'pause {self.filename} lpp {self.last_pause_pos}')
        return self.last_pause_pos

    def unpause(self):
        print(f'unpause {self.filename}')
        self.play(self.last_pause_pos)

class RadioStation(game.Entity):

    STATES = {
        'stopped': 0,
        'playing': 1,
        'paused': 2
    }

    def __init__(self, *args, **kwargs):
        super(RadioStation, self).__init__((10, 10), *args, **kwargs)
        self.state = self.STATES['stopped']
        self.files = self.load_files()
        self.filename = False
        self.last_pause_time = False
        self.last_pause_pos = False
        pygame.mixer.music.set_endevent(config.EVENTS['SONG_END'])

    def play_random(self):
        f = choice(self.files)
        self.last_pause_time = False
        self.last_pause_pos = False
        self.player = MusicPlayer(f)
        self.player.play()
        self.state = self.STATES['playing']

    def play(self):
        if self.state == self.STATES['paused']:
            if self.player:
                if self.last_pause_time:
                    time_delta = time.time() - self.last_pause_time
                    if not self.player.play(self.last_pause_pos + time_delta):
                        self.play_random()
                else:
                    self.player.unpause()
            self.state = self.STATES['playing']
        else:
            self.play_random()

    def pause(self):
        self.state = self.STATES['paused']
        if self.player:
            self.last_pause_time = time.time()
            self.last_pause_pos = self.player.pause()

    def stop(self):
        self.state = self.STATES['stopped']
        if self.player:
            self.player.pause()

    def load_files(self):
        files = []
        for f in os.listdir(self.directory):
            if f.endswith(".mp3") or f.endswith(".ogg") or f.endswith(".wav"):
                files.append(self.directory + f)
        print(files)
        return files

class DiamondCityRadio(RadioStation):
    def __init__(self, *args, **kwargs):
        self.label = 'Diamond City Radio'
        self.directory = 'sounds/radio/DCR/'
        super(DiamondCityRadio, self).__init__(self, *args, **kwargs)

class EnclaveRadio(RadioStation):
    def __init__(self, *args, **kwargs):
        self.label = 'Enclave Radio'
        self.directory = 'sounds/radio/Enclave/'
        super(EnclaveRadio, self).__init__(self, *args, **kwargs)

class InstituteRadio(RadioStation):
    def __init__(self, *args, **kwargs):
        self.label = 'Institute Radio'
        self.directory = 'sounds/radio/Institute/'
        super(InstituteRadio, self).__init__(self, *args, **kwargs)

class MinutemenRadio(RadioStation):
    def __init__(self, *args, **kwargs):
        self.label = 'Minutemen Radio'
        self.directory = 'sounds/radio/Minutemen/'
        super(MinutemenRadio, self).__init__(self, *args, **kwargs)

class Vault101Radio(RadioStation):
    def __init__(self, *args, **kwargs):
        self.label = 'Vault 101 PA System'
        self.directory = 'sounds/radio/V101/'
        super(Vault101Radio, self).__init__(self, *args, **kwargs)

class AgathaRadio(RadioStation):
    def __init__(self, *args, **kwargs):
        self.label = 'Agatha\'s Station'
        self.directory = 'sounds/radio/Violin/'
        super(AgathaRadio, self).__init__(self, *args, **kwargs)

class GNRadio(RadioStation):
    def __init__(self, *args, **kwargs):
        self.label = 'Galaxy News Radio'
        self.directory = 'sounds/radio/gnr/'
        super(GNRadio, self).__init__(self, *args, **kwargs)

# Potential TODO:
# For each station, maintain a RNG and its starting seed.
# Also build up a structure with all of the metadata for all
# of the available tracks.
# Whenever asked to unpause, reset the RNG with the saved seed
# and perform a random walk through the tracks (essentially a
# never ending playlist) until reaching the current time point.
# Provide some mechanism to prevent this from taking a long time.
# Probably the easiest would be to also keep track of the last
# time the station was playing, and if asked to play after some
# threshhold after that time, just start over.
# Or just build a shuffled playlist and work through it until
# it's all played, then reshuffle. Probably better anyways, 
# less repeating of songs.
