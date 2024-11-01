import pypboy


class Module(pypboy.SubModule):
    label = "Quests"

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        self.menu = pypboy.ui.Menu(300,
                                   ["Crucible",
                                    "All Hallow's Eve",
                                    "When Pigs Fly",
                                    "Pyromaniac",
                                    "Speak of the Devil",
                                    "Echoes of the Past",
                                    "Best of Three",
                                    "Ablutions",
                                    ],
                                   [self.show_it,
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
