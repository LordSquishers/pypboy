import pypboy
import pygame
import game
import config


class Module(pypboy.SubModule):
    label = "Ammo"

    items = [".308 Round (186)",
             ".44 Round (94)",
             ".45 Round (421)",
             ".50 Caliber (40)",
             "10mm Round (397)",
             "5.56 Round (368)",
             "5mm Round (181)",
             "Fusion Core (28)",
             "Mini Nuke (3)",
             ]

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        self.menu = pypboy.ui.Menu(300,
                                   self.items,
                                   [self.show_it() for _ in range(len(self.items))],
                                   0)
        self.menu.rect[0] = 4
        self.menu.rect[1] = 60
        self.add(self.menu)

    def show_it(self):
        print("yea");
