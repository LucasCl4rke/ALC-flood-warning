from geo_stations_by_distance import build_station_list

from geo_rivers_by_station_number import stations_by_river_number

N = 9

river_station_dict = stations_by_river_number(build_station_list(), N)

river_station_dict = {key: len(value) for key, value in river_station_dict.items()}

river_n_list = []
for key, count in river_station_dict.items():
    river_n_list.append((key, count))

sorted_river_n_list = sorted(river_n_list, key=lambda x: x[1], reverse=True)


topN_river_N_list = sorted_river_n_list[:N]


print('The N rivers with greatest number of monitoring stations:',topN_river_N_list)