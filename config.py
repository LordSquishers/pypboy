import pygame
import yaml
import confuse

user_config = confuse.Configuration('pypboy', 'pypboy')

EVENTS = {
    'SONG_END': pygame.USEREVENT + 1
}

valid_actions = {
    'module_stats', 
    'module_items',
    'module_data',
    'knob_1',
    'knob_2',
    'knob_3',
    'knob_4',
    'knob_5',
    'dial_up',
    'dial_down',
}

KEY_ACTIONS = {}
key_bindings = user_config['key_bindings'].get()
for key, binding in key_bindings.items():
    if binding in valid_actions:
        key_name = 'K_' + key
        pg_key = getattr(pygame, key_name, False)
        if pg_key:
            KEY_ACTIONS[pg_key] = binding
        else:
            print(f"Invalid key binding: {key}, ignoring.")
    else:
        print(f"Invalid key binding action: {binding}, ignoring.")

# Using GPIO.BCM as mode
GPIO_ACTIONS = {
#    4: "module_stats",  # GPIO 4
#    14: "module_items",  # GPIO 14
#    15: "module_data",  # GPIO 15
#    17:	"knob_1",  # GPIO 17
#    18: "knob_2",  # GPIO 18
#    7: "knob_3",  # GPIO 7
#    22: "knob_4",  # GPIO 22
#    23: "knob_5",  # GPIO 27
    #	31: "dial_up", #GPIO 23
#    27: "dial_down"  # GPIO 7
}

MAP_ICONS = {
    "camp": 		pygame.image.load('images/map_icons/camp.png'),
    "factory": 		pygame.image.load('images/map_icons/factory.png'),
    "metro": 		pygame.image.load('images/map_icons/metro.png'),
    "misc": 		pygame.image.load('images/map_icons/misc.png'),
    "monument": 	pygame.image.load('images/map_icons/monument.png'),
    "vault": 		pygame.image.load('images/map_icons/vault.png'),
    "settlement": 	pygame.image.load('images/map_icons/settlement.png'),
    "ruin": 		pygame.image.load('images/map_icons/ruin.png'),
    "cave": 		pygame.image.load('images/map_icons/cave.png'),
    "landmark": 	pygame.image.load('images/map_icons/landmark.png'),
    "city": 		pygame.image.load('images/map_icons/city.png'),
    "office": 		pygame.image.load('images/map_icons/office.png'),
    "sewer": 		pygame.image.load('images/map_icons/sewer.png'),
}

AMENITIES = {
    'pub': 				MAP_ICONS['vault'],
    'nightclub': 		MAP_ICONS['vault'],
    'bar': 				MAP_ICONS['vault'],
    'fast_food': 		MAP_ICONS['sewer'],
    'cafe': 			MAP_ICONS['sewer'],
    'drinking_water': 	MAP_ICONS['sewer'],
    'restaurant': 		MAP_ICONS['settlement'],
    'cinema': 			MAP_ICONS['office'],
    'pharmacy': 		MAP_ICONS['office'],
    'school': 			MAP_ICONS['office'],
    'bank': 			MAP_ICONS['monument'],
    'townhall': 		MAP_ICONS['monument'],
    'bicycle_parking': 	MAP_ICONS['misc'],
    'place_of_worship': MAP_ICONS['misc'],
    'theatre': 			MAP_ICONS['misc'],
    'bus_station': 		MAP_ICONS['misc'],
    'parking': 			MAP_ICONS['misc'],
    'fountain': 		MAP_ICONS['misc'],
    'marketplace': 		MAP_ICONS['misc'],
    'atm': 				MAP_ICONS['misc'],
}

pygame.font.init()
FONTS = {}
for x in range(10, 28):
    FONTS[x] = pygame.font.Font('monofonto.ttf', x)

def gpioAvailable():
    try:
        __import__("RPi.GPIO") 
    except ImportError:
        return False
    else:
        return True
