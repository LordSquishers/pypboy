import pypboy
import pygame
import game
import config


class Module(pypboy.SubModule):

    label = " Weapons "

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        self.menu = pypboy.ui.Menu(300,
                                   ["December's Child",
                                    "Explosive Heavy Combat Rifle",
                                    "Gamma Gun",
                                    "Night-Vision Quad Barrel Missile Launcher",
                                    "The Ripper",
                                    ],
                                   [self.show_it,
                                    self.show_it,
                                    self.show_it,
                                    self.show_it,
                                    self.show_it,
                                    ],
                                   0)
        self.menu.rect[0] = 4
        self.menu.rect[1] = 60
        self.add(self.menu)

    def show_it(self):
        print("yea");
