from geo_stations_by_distance import build_station_list

from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations

inconsistent_stations = inconsistent_typical_range_stations(build_station_list())

inconsistent_stations_sorted = sorted(inconsistent_stations)

print('Alphabetically sorted list of stations with inconsistent data:',inconsistent_stations_sorted)
