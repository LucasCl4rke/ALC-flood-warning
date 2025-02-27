stations_arb_data = [
  {
    "name": "Bridgeford Station",
    "town": "Bridgeford",
    "river": "River Elwin",
    "typical_low": 1.2,
    "typical_high": 4.5,
    "current_river_level": 3.8,
    "rate_of_river_level_growth": 0.2
  },
  {
    "name": "Westvale Station",
    "town": "Westvale",
    "river": "River Orlan",
    "typical_low": 0.8,
    "typical_high": 3.9,
    "current_river_level": 2.7,
    "rate_of_river_level_growth": -0.1
  },
  {
    "name": "Northgate Station",
    "town": "Northgate",
    "river": "River Sylva",
    "typical_low": 1.5,
    "typical_high": 5.0,
    "current_river_level": 4.2,
    "rate_of_river_level_growth": 0.3
  },
  {
    "name": "Eastbrook Station",
    "town": "Eastbrook",
    "river": "River Arden",
    "typical_low": 0.9,
    "typical_high": 4.2,
    "current_river_level": 3.1,
    "rate_of_river_level_growth": -0.2
  },
  {
    "name": "Sunset Station",
    "town": "Sunsetville",
    "river": "River Mist",
    "typical_low": 3.5,
    "typical_high": 2.9,
    "current_river_level": 1.8,
    "rate_of_river_level_growth": 0.1
  },
  {
    "name": "Hillside Station",
    "town": "Hillside",
    "river": "River Glade",
    "typical_low": 2.1,
    "typical_high": 4.8,
    "current_river_level": None,
    "rate_of_river_level_growth": 0.0
  }
]

for station in stations_arb_data:
    name = station["name"]
    town = station["town"]
    river  = station["river"]
    typical_low = station["typical_low"]
    typical_high = station["typical_high"]
    current_river_level = station["current_river_level"]
    rate_of_river_level_growth = station["rate_of_river_level_growth"]


def run():
   
    relative_water_level_list = []

    for station in stations_arb_data:
        name = station["name"]
        typical_low = station["typical_low"]
        typical_high = station["typical_high"]
        current_river_level = station["current_river_level"]
        if current_river_level is not None and typical_low < typical_high:
            relative_level = (current_river_level - typical_low)/(typical_high - typical_low)
            relative_water_level_list.append((name, relative_level))

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


def test_station_level_over_threshold():
    station_level_over_particular_threshold = station_level_over_threshold(relative_water_level_list2, 0.7)

    n = []
    for i in range(len(station_level_over_particular_threshold)):
        n.append(station_level_over_particular_threshold[i][0])

    assert n == ['Bridgeford Station', 'Northgate Station']






            




