from floodsystem.stationdata import build_station_list

from geo_stations_within_radius import stations_within_radius   

# import math 

from haversine import haversine, Unit

def stations_within_radius(stations, centre, r):
    station_radius_list1 = []
    for station in stations:
        if haversine(station.coord, centre) <= r:
            
            station_radius_list1.append(station.name)
            
    alpha_sorted = sorted(station_radius_list1)

    return alpha_sorted

# changeable point p

centre = (52.2053, 0.1218)

r = 10 

stations = build_station_list()

alpha_sorted = stations_within_radius(stations, centre, r)

assert alpha_sorted == ['Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool", 'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton', 'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']

print("Test passed for stations_within_radius")