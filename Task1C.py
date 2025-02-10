from geo_stations_by_distance import stations_by_distance, build_station_list 

from geo_stations_within_radius import stations_within_radius

# changeable point p

centre = (52.2053, 0.1218)

r = 10 

stations = build_station_list()

alpha_sorted = stations_within_radius(stations, centre, r)

print("Stations within radius r of centre are:", alpha_sorted)