import pypboy
import pygame
import game
import config


class Module(pypboy.SubModule):

    label = "Perks"

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        self.menu = pypboy.ui.Menu(100,
                                   ["Action Boy",
                                    "Astoundingly Awesome 7",
                                    "Awareness",
                                    "Barbarian",
                                    "Cap Collector (2)",
                                    "Covert Operations",
                                    "Guns and Bullets (3)",
                                    "Hacker",
                                    "Lady Killer",
                                    "Live & Love 5",
                                    ],
                                   [self.show_it,
                                    self.show_it,
                                    self.show_it,
                                    self.show_it,
                                    self.show_it,
                                    self.show_it,
                                    self.show_it,
                                    self.show_it,
                                    self.show_it,
                                    self.show_it
                                    ],
                                   0)
        self.menu.rect[0] = 4
        self.menu.rect[1] = 60
        self.add(self.menu)

    def show_it(self):
        print("yea");
