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
        pygame.mixer.music.load(filename)

    def play(self, start_pos = 0):
        self.playing = True
        self.last_start = time.time()
        pygame.mixer.music.load(self.filename)
        pygame.mixer.music.play(0, start_pos)

    def pause(self):
        self.playing = False
        self.last_pause_pos += time.time() - self.last_start
        pygame.mixer.music.stop()

    def unpause(self):
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
        pygame.mixer.music.set_endevent(config.EVENTS['SONG_END'])

    def play_random(self):
        f = choice(self.files)
        self.player = MusicPlayer(f)
        self.player.play()
        self.state = self.STATES['playing']

    def play(self):
        if self.state == self.STATES['paused']:
            if self.player:
                self.player.unpause()
            self.state = self.STATES['playing']
        else:
            self.play_random()

    def pause(self):
        self.state = self.STATES['paused']
        if self.player:
            self.player.pause()

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
