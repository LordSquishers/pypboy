import pygame
import pypboy
from config import user_config

from pypboy.modules.data import entities


class Module(pypboy.SubModule):

	label = "World Map"

	def __init__(self, *args, **kwargs):
		super(Module, self).__init__(*args, **kwargs)

		screen_width = user_config['video']['width'].get()
		screen_height = user_config['video']['height'].get()

		mapgrid = entities.Map(480, pygame.Rect(0, 0, screen_width - 8, screen_height - 80))

		location = (user_config['map']['latitude'].get(), user_config['map']['longitude'].get())

		mapgrid.fetch_map(location, 0.01)
		self.add(mapgrid)
		mapgrid.rect[0] = 4
		mapgrid.rect[1] = 40

	def handle_resume(self):
		self.parent.pypboy.header.headline = "DATA"
		self.parent.pypboy.header.title = "Belfast City"
		super(Module, self).handle_resume()