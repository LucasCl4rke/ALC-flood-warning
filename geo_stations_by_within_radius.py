# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from geo_stations_by_distance import stations_by_distance, build_station_list 

from haversine import haversine, Unit

def stations_within_radius(stations, centre, r):
    station_radius_list1 = []
    for station in stations:
        if haversine(station.coord, centre) <= r:
            
            station_radius_list1.append(station.name)
            
    alpha_sorted = sorted(station_radius_list1)

    return alpha_sorted

    