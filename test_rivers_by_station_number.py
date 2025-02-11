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

def test_rivers_by_station_number():

    N = 3

    river_station_dict = rivers_by_station_number(build_station_list(), N)

    river_station_dict = {key: len(value) for key, value in river_station_dict.items()}

    river_n_list = []
    for key, count in river_station_dict.items():
        river_n_list.append((key, count))

    sorted_river_n_list = sorted(river_n_list, key=lambda x: x[1], reverse=True)


    topN_river_N_list = sorted_river_n_list[:N]


    assert topN_river_N_list == [('River Thames', 55), ('River Avon', 32), ('River Great Ouse', 30)]

