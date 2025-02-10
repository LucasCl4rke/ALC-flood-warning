from floodsystem.stationdata import build_station_list

from geo_stations_by_distance import stations_by_distance

import math 

def test_stations_by_distance():
    
    stations = build_station_list()[:1]

   
    p = (50.0, 0.0)

    # Call the function
    result1 = stations_by_distance(stations, p)

    result2 = result1[0]

    result3 = result2[2]


    assert round(result3, 4) == 90.9699

    # print(result2)
    # print(result3)
    # print(build_station_list()[:1])

    print("Test passed")
    print(build_station_list()[:1])


test_stations_by_distance()