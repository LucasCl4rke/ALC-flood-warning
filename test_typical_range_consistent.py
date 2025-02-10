from floodsystem.stationdata import build_station_list

from floodsystem.station import MonitoringStation

stations = build_station_list()

print(stations[0])

assert stations[0].typical_range_consistent() == True

print("Test passed for typical_range_consistent")