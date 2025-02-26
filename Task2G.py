from floodsystem.stationdata import build_station_list, update_water_levels


def run():
    stations = build_station_list()

    update_water_levels(stations)
    
    relative_water_level_list = []

    for station in stations:
        if station.latest_level is not None and station.typical_range_consistent():
            relative_level = station.relative_water_level()
            if relative_level is not None:
                relative_water_level_list.append((station.name, relative_level))

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

station_level_severe = station_level_over_threshold(relative_water_level_list2, 2)

station_level_over_particular_threshold = station_level_over_threshold(relative_water_level_list2, 1.5)
station_level_over_particular_threshold = [station for station in station_level_over_particular_threshold if station[1] <= 2]

station_level_over_particular_threshold2 = station_level_over_threshold(relative_water_level_list2, 1.3)
station_level_over_particular_threshold2 = [station for station in station_level_over_particular_threshold2 if station[1] <= 1.5]

station_level_over_particular_threshold3 = station_level_over_threshold(relative_water_level_list2, 1.0)
station_level_over_particular_threshold3= [station for station in station_level_over_particular_threshold3 if station[1] <= 1.3]

station_level_over_particular_threshold4 = station_level_over_threshold(relative_water_level_list2, 0.0)
station_level_over_particular_threshold4= [station for station in station_level_over_particular_threshold4 if station[1] <= 1.0]


potentially_dangerous_names = [station[0] for station in station_level_over_particular_threshold]


station_over_particular_tol_list = []
for station in station_level_over_particular_threshold:
    station_over_particular_tol_list.append(station[0])


station_over_particular_tol_list2 = []
for station in station_level_over_particular_threshold2:
    station_over_particular_tol_list2.append(station[0])


station_over_particular_tol_list3 = []
for station in station_level_over_particular_threshold3:
    station_over_particular_tol_list3.append(station[0])


station_over_particular_tol_list4 = []
for station in station_level_over_particular_threshold4:
    station_over_particular_tol_list4.append(station[0])



# work from here


import datetime

from floodsystem.datafetcher import fetch_measure_levels

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

    dt = 1
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
        if level is not None and isinstance(level, (int, float)) and level > 0:
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

    poly_derivative = np.polyder(poly)

    x_max = x[-1]

    derivative_at_xmax = poly_derivative(x_max)

    return (station, derivative_at_xmax)

station_level_severe_names = []
for i in range(len(station_level_severe)):
    station_level_severe = station_level_over_threshold(relative_water_level_list2, 2)
    station_level_severe_names.append(station_level_severe[i][0])

station_level_high_names = []
for station_name in station_over_particular_tol_list:

    if date_level(station_name)[0] is not None and date_level(station_name)[1] is not None:
        dates = date_level(station_name)[0]
        polyfit_x = mdates.date2num(dates)
        if polyfit(station_name, polyfit_x, date_level(station_name)[1], 4)[1] > 0.2:
            station_level_severe_names.append(station_name)
        else:
            station_level_high_names.append(station_name)


station_level_moderate_names = []
for station_name in station_over_particular_tol_list2:
    date_levels = date_level(station_name)
    if date_level(station_name)[0] is not None and date_level(station_name)[1] is not None:
        dates = date_level(station_name)[0]
        polyfit_x = mdates.date2num(dates)
        if polyfit(station_name, polyfit_x, date_level(station_name)[1], 4)[1] > 0.2:
            station_level_high_names.append(station_name)
        else:
            station_level_moderate_names.append(station_name)


station_level_low_names = []
for station_name in station_over_particular_tol_list3:
    if date_level(station_name)[0] is not None and date_level(station_name)[1] is not None:
        dates = date_level(station_name)[0]
        polyfit_x = mdates.date2num(dates)
        if polyfit(station_name, polyfit_x, date_level(station_name)[1], 4)[1] > 0.2:
            station_level_moderate_names.append(station_name)
        else:
            station_level_low_names.append(station_name)


for i in range(len(station_over_particular_tol_list4)):   
    station_level_low_names.append(station_over_particular_tol_list4[i])

stations = build_station_list()  # List of station objects
station_town_map = {station.name: station.town for station in stations if station.town}  # Dictionary mapping station names to towns

town_level_severe_names = []
for station_name in station_level_severe_names:
    town_name = station_town_map.get(station_name)  # Get town name from dictionary
    if town_name and town_name not in town_level_severe_names:
        town_level_severe_names.append(town_name)

town_level_high_names = []
for station_name in station_level_high_names:
    town_name = station_town_map.get(station_name)
    if town_name and town_name not in town_level_high_names:
        town_level_high_names.append(town_name)

town_level_moderate_names = []
for station_name in station_level_moderate_names:
    town_name = station_town_map.get(station_name)
    if town_name and town_name not in town_level_moderate_names:
        town_level_moderate_names.append(town_name)

town_level_low_names = []
for station_name in station_level_low_names:
    town_name = station_town_map.get(station_name)
    if town_name and town_name not in town_level_low_names:
        town_level_low_names.append(town_name)

# Remove duplicates across risk levels: ensure towns appear only in the highest applicable category
town_level_severe_names = set(town_level_severe_names)
town_level_high_names = set(town_level_high_names) - town_level_severe_names
town_level_moderate_names = set(town_level_moderate_names) - town_level_severe_names - town_level_high_names
town_level_low_names = set(town_level_low_names) - town_level_severe_names - town_level_high_names - town_level_moderate_names

# Convert back to lists if needed
town_level_severe_names = list(town_level_severe_names)
town_level_high_names = list(town_level_high_names)
town_level_moderate_names = list(town_level_moderate_names)
town_level_low_names = list(town_level_low_names)


print('Town where risk is Severe:', town_level_severe_names)
print('Towns where risk is High:', town_level_high_names)
print('Towns where risk is Moderate:', town_level_moderate_names)
print('Towns where risk is Low:', town_level_low_names)



