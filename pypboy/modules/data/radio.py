import pypboy
import config

from pypboy.modules.data.radio_stations import RadioStation
from pypboy.modules.data import oscilloscope

class Module(pypboy.SubModule):

	label = "Radio"

	def __init__(self, *args, **kwargs):
		super(Module, self).__init__(*args, **kwargs)

		self.oscilloscope = oscilloscope.Oscilloscope()
		self.add(self.oscilloscope)

		station_info = config.user_config['radio']['stations'].get()
		self.stations = list(map(lambda s: RadioStation(s['label'], s['directory']), station_info))
		for station in self.stations:
			station.set_oscilloscope(self.oscilloscope)
			self.add(station)
		self.active_station = None
		config.radio = self

		stationLabels = []
		stationCallbacks = []
		for i, station in enumerate(self.stations):
			stationLabels.append(station.label)
			stationCallbacks.append(lambda i=i: self.select_station(i))

		self.menu = pypboy.ui.Menu(200, stationLabels, stationCallbacks, 0)
		self.menu.rect[0] = 4
		self.menu.rect[1] = 60
		self.add(self.menu)

		self.menu.select(1)

	def select_station(self, station):
		if hasattr(self, 'active_station') and self.active_station:
			self.active_station.pause()
		self.active_station = self.stations[station]
		self.active_station.play()


	def handle_event(self, event):
		if event.type == config.EVENTS['SONG_END']:
			if hasattr(self, 'active_station') and self.active_station:
				self.active_station.play_random()

	def handle_resume(self):
		self.parent.pypboy.header.headline = "DATA"
		self.parent.pypboy.header.title = "Radio"
		super(Module, self).handle_resume()
		