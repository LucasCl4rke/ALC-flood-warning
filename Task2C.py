from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    stations = build_station_list()

    update_water_levels(stations)
    
    relative_water_level_list = []

    for station in stations:
        if station.latest_level is not None and station.latest_level > 0 and station.typical_range_consistent():
            relative_level = station.relative_water_level()
            if relative_level is not None:
                relative_water_level_list.append((station.name, relative_level))

    return relative_water_level_list

# Had to put funtion in as importing wasnt working properly

relative_water_level_list2 = run()

def stations_highest_rel_level(stations, N):
    highest_relative_water_level = []
    for station in stations:
        if station[1] is not None:
            relative_level = station[1]
            highest_relative_water_level.append((station[0], relative_level))
            sorted_highest_relative_water_level = sorted(highest_relative_water_level, key = lambda x: x[1], reverse = True)
    for i in range(len(sorted_highest_relative_water_level[:N])):
        print(sorted_highest_relative_water_level[i])
    
stations_highest_rel_level(relative_water_level_list2, 10)
