import sys
import os

original_stdout = sys.stdout

sys.stdout = open(os.devnull, 'w')

from geo_stations_by_distance import stations_by_distance, build_station_list

from haversine import haversine, Unit

def stations_by_river_number(stations, N):
    river_station_dict = {}
    for station in stations:
        if station.river in river_station_dict:
            river_station_dict[station.river].append(station.name)
        else:
            river_station_dict[station.river] = [station.name]  

    return river_station_dict  


sys.stdout = original_stdout