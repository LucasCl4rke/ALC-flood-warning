from geo_stations_by_distance import stations_by_distance, build_station_list 

# changeable point p

p = (52.2053, 0.1218)

stations = build_station_list()

sorted_stations = stations_by_distance(stations, p)

station_distance_list2 = []
for i in range(10):
    station_distance_list2.append(sorted_stations[i])

print("Closest 10 stations to p in order are:", station_distance_list2)

n = len(sorted_stations)
station_distance_list3 = []
for i in range(n-10, n):
    station_distance_list3.append(sorted_stations[i])

print("Furthest 10 stations to p in order are:", station_distance_list3)

