# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from geo_stations_by_distance import stations_by_distance, build_station_list 

from haversine import haversine, Unit

def rivers_with_station(stations):
    station_river_list = []
    for station in stations:
        station_river_list.append(station.river)
        station_river_list = list(set(station_river_list))
    
    return station_river_list
    

    