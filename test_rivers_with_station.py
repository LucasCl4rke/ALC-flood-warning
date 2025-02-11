from geo_stations_by_distance import stations_by_distance, build_station_list 

from haversine import haversine, Unit

def rivers_with_station(stations):
    station_river_list = []
    for station in stations:
        station_river_list.append(station.river)
        station_river_list = list(set(station_river_list))

    return station_river_list

def test_rivers_with_station():
    
    stations = build_station_list()[:1]

    assert rivers_with_station(stations) == ['River Dikler']

    



