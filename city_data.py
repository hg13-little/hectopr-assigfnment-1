# city_data.py
# A class for storing a city's population data
# Starter Code from CSC 210
# Modified by: [hector]
class CityData:
    
       def __init__(self, name, start_year, data):
        self._name = name
        self._start_year = start_year
        self._data = data
        self._end_year = start_year + len(data) - 1

    @property
    def name(self):
        return self._name

    def __getitem__(self, year):
        if not isinstance(year, int):
            raise TypeError("Year must be an integer")
        if year < self._start_year or year > self._end_year:
            raise IndexError("Year out of range")
        return self._data[year - self._start_year]
    