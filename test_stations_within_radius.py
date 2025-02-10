from floodsystem.stationdata import build_station_list

from geo_stations_within_radius import stations_within_radius   
import math 

def test_stations_within_radius():
    
    stations = build_station_list()[:1]

    centre = (52.2053, 0.1218)

    # Call the function
    result1 = stations_by_distance(stations, p)

    result2 = result1[0]

    result3 = result2[2]


    assert round(result3, 4) == 90.9699

    # print(result2)
    # print(result3)
    # print(build_station_list()[:1])

    print("Test passed")


test_stations_by_distance()



---------
from geo_stations_by_distance import stations_by_distance, build_station_list 

from haversine import haversine, Unit

def stations_within_radius(stations, centre, r):
    station_radius_list1 = []
    for station in stations:
        if haversine(station.coord, centre) <= r:
            
            station_radius_list1.append(station.name)
            
    alpha_sorted = sorted(station_radius_list1)

    return alpha_sorted
