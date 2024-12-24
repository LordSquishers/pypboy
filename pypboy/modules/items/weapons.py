import pypboy
import pygame
import game
import config


class Module(pypboy.SubModule):

    label = " Weapons "

    items = ["10mm Auto Pistol",
             "Artillery Smoke Grenade (9)",
             "Bloodied Switchblade",
             "Bottlecap Mine (4)",
             "Broadsider",
             "Cryo Mine (3)",
             "Explosive 10mm Pistol",
             "Fat Man",
             "Fragmentation Mine (8)",
             "Long Converted Alien Blaster Pistol",
             "Molotov Cocktail (2)",
             "Plasma Grenade (2)",
             "Pulse Grenade (2)",
             "Pulse Mine (3)",
             "Recon .50 Sniper Rifle",
             "Supressed Calibrated Powerful Sniper Rifle",
             "Wazer Wifle"]

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
