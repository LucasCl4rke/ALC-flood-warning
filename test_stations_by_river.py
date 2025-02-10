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

stations = build_station_list()[:1]

assert stations_by_river(stations) == {'River Dikler': ['Bourton Dickler']}

print("Test passed for stations_by_river")