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

relative_water_level_list2 = run()

def stations_highest_rel_level(stations, N):
    """Returns a sorted list of the N stations with the highest relative water level."""
    highest_relative_water_level = []

    for station in stations:
        if station[1] is not None:
            highest_relative_water_level.append((station[0], station[1]))

    sorted_highest_relative_water_level = sorted(highest_relative_water_level, key=lambda x: x[1], reverse=True)

    return sorted_highest_relative_water_level[:N]

highest_5 = stations_highest_rel_level(relative_water_level_list2, 5)

highest_5_names = [station[0] for station in highest_5]

print("Top 5 stations with highest relative water levels:")
for station in highest_5:
    print(station)

print(highest_5_names)



# work from here


import datetime

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import build_station_list

def date_level(station_name):

    stations = build_station_list()

    station_cam = None
    for station in stations:
        if station.name == station_name:
            station_cam = station
            break

    if not station_cam:
        print("Station {} could not be found".format(station_name))
        return

    dt = 2
    dates, levels = fetch_measure_levels(
        station_cam.measure_id, dt=datetime.timedelta(days=dt))
    
    if not dates or not levels:
        print(f"No water level data available for {station_cam.name}.")
        return

    # Print level history
    date_list = []
    level_list = []
    last_valid_level = None
    for date, level in zip(dates, levels):
        date_list.append(date)
        if level is not None  and level > 0:
            last_valid_level = level
            level_list.append(level)
        else:
            level_list.append(last_valid_level)
            
    return (date_list, level_list)



import matplotlib.dates as mdates



import numpy as np
import matplotlib.pyplot as plt

def polyfit(station, dates, levels, p):

    # Create set of 10 data points on interval (0, 2)
    x = dates
    y = levels

    # Find coefficients of best-fit polynomial f(x) of degree 4
    p_coeff = np.polyfit(x, y, p)

    # Convert coefficient into a polynomial that can be evaluated,
    # e.g. poly(0.3)
    poly = np.poly1d(p_coeff)

    # Plot original data points
    plt.plot(x, y, '.')

    # Plot polynomial fit at 30 points along interval
    x1 = np.linspace(x[0], x[-1], 30)
    plt.plot(x1, poly(x1))
    plt.title(station)

    # Display plot
    plt.show()

for station_name in highest_5_names:
    dates = date_level(station_name)[0]
    polyfit_x = mdates.date2num(dates)
    polyfit(station_name, polyfit_x, date_level(station_name)[1], 4)
