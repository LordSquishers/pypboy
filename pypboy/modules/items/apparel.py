import pypboy
import pygame
import game
import config


class Module(pypboy.SubModule):

    label = " Apparel "

    items = ["Black-Rim Glasses",
             "Formal Hat",
             "Hazmat Suit",
             "Kellogg's Outfit",
             "Lieutenant's Hat",
             "Minutemen General's Uniform",
             "Wedding Ring",
             "Wedding Ring",
             "Worn Fedora"]

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
