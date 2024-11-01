import pypboy
import pygame
import game
import config


class Module(pypboy.SubModule):

    label = "Misc"

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        self.menu = pypboy.ui.Menu(300,
                                   ["A New Path",
                                    "Arcjet Lab Password",
                                    "Associate's Note",
                                    "Astoundingly Awesome Tales",
                                    "Blood Clinic Key",
                                    "Bobby Pin (49)",
                                    "Cabot House Key",
                                    "Charisma Bobblehead",
                                    "Combat Sentry Proto MKIV Holotape",
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
        
