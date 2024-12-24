import pypboy
import pygame
import game
import config

class Module(pypboy.SubModule):
        
    label = "Aid"

    items = ["Carrot Flower",
             "Crispy Squirrel Bits",
             "Deathclaw Meat",
             "Fancy Lads Snack Cakes",
             "Glowing Fungus (6)",
             "Jet (15)",
             "Med-X (2)",
             "Mentats (2)",
             "Mirelurk Cake (5)",
             "Mole Rat Chunks",
             "Nuka-Cherry (7)",
             "Nuka-Cola (4)",
             "Nuka-Cola Quantum (13)",
             "Pork n' Beans",
             "Psycho (11)",
             "Purified Water (29)",
             "Rad-X (75)",
             "RadAway (52)",
             "Radroach Meat (3)",
             "Softshell Mirelurk Meat (2)",
             "Squirrel On A Stick",
             "Stealth Boy (7)"
             "Stimpack (20)",
             "Wild Mutfruit"]

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
