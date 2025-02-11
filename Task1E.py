from geo_stations_by_distance import build_station_list

from geo_rivers_by_station_number import rivers_by_station_number

N = 9

river_station_dict = rivers_by_station_number(build_station_list(), N)

river_station_dict = {key: len(value) for key, value in river_station_dict.items()}

river_n_list = []
for key, count in river_station_dict.items():
    river_n_list.append((key, count))

sorted_river_n_list = sorted(river_n_list, key=lambda x: x[1], reverse=True)


topN_river_N_list = sorted_river_n_list[:N]

g = topN_river_N_list[N-1][1]

for i in range(N, len(sorted_river_n_list)):
    if sorted_river_n_list[i][1] == g:
        topN_river_N_list.append(sorted_river_n_list[i])
    else:
        break


print('The N rivers with greatest number of monitoring stations:',topN_river_N_list)