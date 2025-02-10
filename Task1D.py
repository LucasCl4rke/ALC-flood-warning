from geo_stations_by_distance import build_station_list

from geo_rivers_with_station import rivers_with_station

from geo_stations_by_river import stations_by_river

station_river_list1 = rivers_with_station(build_station_list())
print("Number of stations by river is:", len(station_river_list1))
    
sorter_river = sorted(station_river_list1)
sorted_river_list2 = []
for i in range(10):
    sorted_river_list2.append(sorter_river[i])

print("Stations by river in order are:", sorted_river_list2)



river_station_dict = stations_by_river(build_station_list())

def f(p):
    river = stations_by_river(build_station_list())
    sorted_river = sorted(river[p])
    print(p,'is monitored by these stations:',sorted_river)
            
f('River Aire')
f('River Cam')
f('River Thames')
