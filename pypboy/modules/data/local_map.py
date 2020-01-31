import pygame
import pypboy
from config import config

from pypboy.modules.data import entities


class Module(pypboy.SubModule):

	label = "Local Map"

	def __init__(self, *args, **kwargs):
		super(Module, self).__init__(*args, **kwargs)
		screen_width = config['video']['width'].get()
		screen_height = config['video']['height'].get()

		mapgrid = entities.Map(screen_width, pygame.Rect(4, (screen_width - screen_height) / 2, screen_width - 8, screen_height - 80))

		location = [config['map']['latitude'].get(), config['map']['longitude'].get()]

		mapgrid.fetch_map(location, 0.003)
		self.add(mapgrid)
		mapgrid.rect[0] = 4
		mapgrid.rect[1] = 40

	def handle_resume(self):
		self.parent.pypboy.header.headline = "DATA"
		self.parent.pypboy.header.title = "City Centre"
		super(Module, self).handle_resume()