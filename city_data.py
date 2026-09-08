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

    @property
    def start_year(self):
        return self._start_year

    @property
    def end_year(self):
        return self._end_year

    @property
    def max_year(self):
        biggest = max(self._data)
        position = self._data.index(biggest)
        return self._start_year + position

    @property
    def min_year(self):
        smallest = min(self._data)
        position = self._data.index(smallest)
        return self._start_year + position

    def population_growth(self, start_year, end_year):
        return self[end_year] - self[start_year]

    def __getitem__(self, year):
        if not isinstance(year, int):
            raise TypeError("Year must be an integer")

        if year < self._start_year or year > self._end_year:
            raise IndexError("Year out of range")

        position = year - self._start_year
        return self._data[position]