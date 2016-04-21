#!/usr/bin/python
import math

# Get the angle between 2 coordinates

def getAngleByCoordinates(coLocal, coRemote):

    lat1 = math.radians(coLocal[0])
    lat2 = math.radians(coRemote[0])

    diffLong = math.radians(coRemote[1] - coLocal[1])

    x = math.sin(diffLong) * math.cos(lat2)
    y = math.cos(lat1) * math.sin(lat2) - (math.sin(lat1) * math.cos(lat2) * math.cos(diffLong))

    initial_bearing = math.degrees(math.atan2(x, y))
    compass_bearing = (initial_bearing + 360) % 360
    dest = int(round(compass_bearing))
    return dest

pointA = (1.111, 1.111)     # Latitude, Longtitude
pointB = (1.111, 1.111)     # Latitude, Longtitude

print(getAngleByCoordinates(pointA, pointB))