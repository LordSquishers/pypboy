import config
import threading
import time
from config import user_config
if config.gpsAvailable():
    from gps import *
    gpsAvailable = True
else:
    gpsAvailable = False
    
class LocationManager:
    _latitude = 0
    _longitude = 0
    _gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
    _lock = threading.Lock()

    def __init__(self):
        if gpsAvailable:
            self._thread = threading.Thread(target=self.gpsThread)
            self._thread.start()

    def gpsThread(self):
        while True:
            nx = self._gpsd.next()
            if nx['class'] == 'TPV':
                self._lock.acquire()
                self._latitude = getattr(nx,'lat', "Unknown")
                self._longitude = getattr(nx,'lon', "Unknown")
                print(self._latitude)
                self._lock.release()
            time.sleep(10)

    def getPositionData(self):
        if gpsAvailable:
            self._lock.acquire()
            latitude = self._latitude
            longitude = self._longitude
            self._lock.release()
        else:
            latitude = user_config['map']['latitude'].get(int)
            longitude = user_config['map']['longitude'].get(int)

        return (longitude, latitude)
