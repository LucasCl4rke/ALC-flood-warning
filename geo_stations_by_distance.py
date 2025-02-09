# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

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

