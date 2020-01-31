import pygame
import pypboy
import config as oldconfig
from config import config

from pypboy.modules.data import entities


class Module(pypboy.SubModule):

	label = "World Map"

	def __init__(self, *args, **kwargs):
		super(Module, self).__init__(*args, **kwargs)

		screen_width = config['video']['width'].get()
		screen_height = config['video']['height'].get()

		mapgrid = entities.Map(480, pygame.Rect(0, 0, screen_width - 8, screen_height - 80))
		mapgrid.fetch_map(oldconfig.MAP_FOCUS, 0.01)
		self.add(mapgrid)
		mapgrid.rect[0] = 4
		mapgrid.rect[1] = 40

	def handle_resume(self):
		self.parent.pypboy.header.headline = "DATA"
		self.parent.pypboy.header.title = "Belfast City"
		super(Module, self).handle_resume()