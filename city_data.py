# city_data.py
# A class for storing a city's population data
# Starter Code from CSC 210
# Modified by: [Your Name]

class CityData:
    # YOUR CODE HERE
    # Reverse engineer what is expected here
    # based on main.py, and tests.py
    # a couple methods/properties are already done for you;
    # don't forget to make your constructor and to;

    @property
    def name(self):
        return self._name

    def __getitem__(self, year):
        if not isinstance(year, int):
            raise TypeError("Year must be an integer")
        if year < self._start_year or year > self._end_year:
            raise IndexError("Year out of range")
        return self._data[year - self._start_year]
    