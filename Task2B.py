from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.station import MonitoringStation, relative_water_level_list

relative_water_levels_listed = relative_water_level_list(build_station_list())

def run():
    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)
    
    # Initialize an empty list to store (station name, relative level) tuples
    relative_water_level_list = []

    for station in stations:
        if station.latest_level is not None and station.typical_range_consistent():
            relative_level = station.relative_water_level()
            if relative_level is not None:
                relative_water_level_list.append((station.name, relative_level))

    # Print the full list of stations with their relative water levels
    return relative_water_level_list

relative_water_level_list2 = run()

def station_level_over_threshold(stations, tol):
    stations_over_threshold = []
    for station in stations:
        if station[1] is not None and station[1] > tol:
            relative_level = station[1]
            stations_over_threshold.append((station[0], relative_level))
            stations_over_threshold_sorted = sorted(stations_over_threshold, key = lambda x: x[1], reverse = True)
    return stations_over_threshold_sorted

station_level_over_particular_threshold = station_level_over_threshold(relative_water_level_list2, 0.8)

for i in range(len(station_level_over_particular_threshold)):
    print(station_level_over_particular_threshold[i])

