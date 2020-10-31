import pypboy
from alsaaudio import Mixer

class Module(pypboy.SubModule):

	label = "Misc"

	def __init__(self, *args, **kwargs):
		super(Module, self).__init__(*args, **kwargs)

		items = []
		actions = []
		for i in range(0, 8):
			name = 'Volume ' + str(i)
			items.append(name)
			action = lambda i=i: self.set_volume(i)
			actions.append(action)

		self.menu = pypboy.ui.Menu(100, items, actions, 0)
		self.menu.rect[0] = 4
		self.menu.rect[1] = 60
		self.add(self.menu)

	def set_volume(self, i):
		print(f"set volume {i}")
		Mixer('Headphone').setvolume(i * 12)
