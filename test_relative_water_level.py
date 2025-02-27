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


def relative_water_level(stations):
    for station in stations:
        typical_low = station["typical_low"]
        typical_high = station["typical_high"]
        current_river_level = station["current_river_level"]
        if typical_low < typical_high and current_river_level is not None:
            a = (current_river_level - typical_low) / (typical_high - typical_low)
            return a
        else:
            return None
            
print(relative_water_level(stations_arb_data[:1]))
print(stations_arb_data[:1])
    

actual_rel_level_Bridgeford_Station = (3.8 - 1.2)/(4.5 - 1.2)
expected = round(actual_rel_level_Bridgeford_Station, 5)

def test_relative_water_level():
    
    stations = stations_arb_data[:1]
    result = round(relative_water_level(stations), 5)

    assert result == expected



        

