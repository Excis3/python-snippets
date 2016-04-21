#!/usr/bin/python
from math import radians, cos, sin, asin, sqrt

# Calculate distance between 2 points
AVG_EARTH_RADIUS = 6371  # in km

def haversine(point1, point2):

    # unpack latitude/longitude
    lat1, lng1 = point1
    lat2, lng2 = point2

    # convert all latitudes/longitudes from decimal degrees to radians
    lat1, lng1, lat2, lng2 = map(radians, (lat1, lng1, lat2, lng2))

    # calculate haversine
    lat = lat2 - lat1
    lng = lng2 - lng1
    d = sin(lat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(lng * 0.5) ** 2
    h = 2 * AVG_EARTH_RADIUS * asin(sqrt(d))

    return h  # in kilometers



p1 = (1.111, 1.111)      # Latitude, Longtitude
p2 = (1.111, 1.111)      # Latitude, Longtitude
length = haversine(p1, p2)

print(length)
