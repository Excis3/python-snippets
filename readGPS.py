#!/usr/bin/python
import threading
import time
from gps import *

class GpsController(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.gpsd = gps(mode=WATCH_ENABLE)
        self.running = True

    def run(self):
        while self.running:
            # grab EACH set of gpsd info to clear the buffer
            self.gpsd.next()

    def stopController(self):
        self.running = False

    @property
    def fix(self):
        return self.gpsd.fix


def gpsthread():
    gotGPS = True
    cnt = 0
    longList = []
    latList = []

    gpsc = GpsController()
    gpsc.start()  # start it up

    while gotGPS:
        lat = gpsc.fix.latitude
        long = gpsc.fix.longitude

        latList.append(lat)     # store in list
        longList.append(long)
        cnt += 1

        # got 6 reads.
        if cnt == 6:
            gotGPS = False
            gpsc.stopController()
            gpsc.join()

        time.sleep(2)  # set to whatever

        # get avarage point location
        lat = sum(latList)/len(latList)
        long = sum(longList)/len(longList)

        print(lat)
        print(long)
