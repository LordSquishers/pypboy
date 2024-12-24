import pypboy
import pygame
import game
import config


class Module(pypboy.SubModule):
    label = "Misc"

    items = ["Bobby Pin (50)",
             "Duct Tape (4)",
             "Fuse",
             "Giddyup Buttercup (4)",
             "Grognak the Barbarian",
             "Jangles The Moon Monkey",
             "Mr. Gutsy Model",
             "Pre-War Money (26)",
             "Reactor Terminal Password (2)",
             "Tin Can (9)"]

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
