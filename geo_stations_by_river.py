# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

# Had to nuke the print function from this file as was causing random unnecessary print statements to appear in tasks. 
# We could not find the source of the print statements in this file.

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