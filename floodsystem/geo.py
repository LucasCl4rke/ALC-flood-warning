# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""
from .utils import sorted_by_key  # noqa

from floodsystem.utils import sorted_by_key  # noqa

from floodsystem.stationdata import build_station_list

from haversine import haversine, Unit

def stations_by_distance(stations, p):
    """Requirements for Task 1A"""

    # Build list of stations
    stations = build_station_list()
    station_distance_list1 = []
    for station in stations:
            
        distance_to_p = haversine(station.coord, p)

        station_name_town_distance = (station.name, station.town, distance_to_p)

        station_distance_list1.append(station_name_town_distance)      

    sorted_stations = sorted_by_key(station_distance_list1, 2, reverse=False)

    return sorted_stations

from geo_stations_by_distance import stations_by_distance, build_station_list 

from haversine import haversine, Unit

def stations_within_radius(stations, centre, r):
    station_radius_list1 = []
    for station in stations:
        if haversine(station.coord, centre) <= r:
            
            station_radius_list1.append(station.name)
            
    alpha_sorted = sorted(station_radius_list1)

    return alpha_sorted


from geo_stations_by_distance import stations_by_distance, build_station_list 

from haversine import haversine, Unit

def rivers_with_station(stations):
    station_river_list = []
    for station in stations:
        station_river_list.append(station.river)
        station_river_list = list(set(station_river_list))
    
    return station_river_list

import sys
import os

original_stdout = sys.stdout

sys.stdout = open(os.devnull, 'w')

from geo_stations_by_distance import stations_by_distance, build_station_list 

from haversine import haversine, Unit

def stations_by_river(stations):
    river_station_dict = {}
    for station in stations:
        if station.river in river_station_dict:
            river_station_dict[station.river].append(station.name)
        else:
            river_station_dict[station.river] = [station.name]  

    return river_station_dict  


sys.stdout = original_stdout



import sys
import os

original_stdout = sys.stdout

sys.stdout = open(os.devnull, 'w')

from geo_stations_by_distance import stations_by_distance, build_station_list

from haversine import haversine, Unit

def rivers_by_station_number(stations, N):
    river_station_dict = {}
    for station in stations:
        if station.river in river_station_dict:
            river_station_dict[station.river].append(station.name)
        else:
            river_station_dict[station.river] = [station.name]  

    return river_station_dict  


sys.stdout = original_stdout
