import pytest
from geo_stations_by_distance import build_station_list

def stations_by_river(stations):
   
    river_station_dict = {}
    for station in stations:
        if station.river in river_station_dict:
            river_station_dict[station.river].append(station.name)
        else:
            river_station_dict[station.river] = [station.name]
    return river_station_dict

def test_stations_by_river():
    
    stations = build_station_list()[:1] 
    result = stations_by_river(stations)
    
    expected = {'River Dikler': ['Bourton Dickler']}
    assert result == expected, f"Expected {expected}, but got {result}"
