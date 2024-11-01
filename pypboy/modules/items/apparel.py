import pypboy
import pygame
import game
import config


class Module(pypboy.SubModule):

    label = " Apparel "

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        self.menu = pypboy.ui.Menu(300,
                                   ["Acadia's Shield",
                                    "Atom's Bukwark",
                                    "High Confessor's Helo",
                                    "High Confessor's Robes",
                                    "Minutemen General's Hat",
                                    "Minutemen General's Uniform",
                                    "Postman's Hat",
                                    "Vault Jumpsuit",
                                    ],
                                   [self.show_it,
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
