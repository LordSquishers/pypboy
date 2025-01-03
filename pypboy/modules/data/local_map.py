import pygame
import pypboy
from config import user_config

from pypboy.modules.data import entities


class Module(pypboy.SubModule):

	label = "Local Map"
	
	def __init__(self, *args, **kwargs):
		super(Module, self).__init__(*args, **kwargs)
		screen_width = user_config['video']['width'].get()
		screen_height = user_config['video']['height'].get()

		mapgrid = entities.Map(screen_width, 0.003, pygame.Rect(4, (screen_width - screen_height) / 2, screen_width - 8, screen_height - 80))

		location = (user_config['map']['latitude'].get(float), user_config['map']['longitude'].get(float))
		mapgrid.fetch_map(location, 0.003)  # ~800m diameter
		self.add(mapgrid)
		mapgrid.rect[0] = 4
		mapgrid.rect[1] = 40

	def handle_resume(self):
		self.parent.pypboy.header.headline = "DATA"
		self.parent.pypboy.header.title = "Local Area"
		super(Module, self).handle_resume()
