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

def run(station_name):

    stations = build_station_list()

    station_cam = None
    for station in stations:
        if station.name == station_name:
            station_cam = station
            break

    if not station_cam:
        print("Station {} could not be found".format(station_name))
        return

    dt = 10
    dates, levels = fetch_measure_levels(
        station_cam.measure_id, dt=datetime.timedelta(days=dt))
    
    if not dates or not levels:
        print(f"No water level data available for {station_cam.name}.")
        return

    # Print level history
    date_list = []
    level_list = []
    for date, level in zip(dates, levels):
        date_list.append((date))
        if level > 0:
            level_list.append((level))
        else:
            level_list.append(None)
    return (date_list, level_list)


import matplotlib.pyplot as plt

def plot_water_levels(station, dates, levels):

    t = dates
    level = levels

    # Plot
    plt.plot(t, level, color='b', label="Water level")

    stations = build_station_list()

    for station in stations:
        if station.name == station_name:
            plt.axhline(y=station.typical_range[0], color='g', linestyle='--', label="Typical Low")
            plt.axhline(y=station.typical_range[1], color='r', linestyle='--', label="Typical High")
            break

    # Add axis labels, rotate date labels and add plot title
    plt.xlabel('date')
    plt.ylabel('water level (m)')
    plt.xticks(rotation=45);
    plt.title(station.name)
    plt.legend()

    # Display plot
    plt.tight_layout()  # This makes sure plot does not cut off date labels

    plt.show()

for station_name in highest_5_names:
    plot_water_levels(station_name, run(station_name)[0], run(station_name)[1])
    