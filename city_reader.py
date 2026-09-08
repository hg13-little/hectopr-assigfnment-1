# city_reader.py
# Read the city data from a CSV File
# Starter Code from CSC 210
# Modified by: [hector]

from csv import DictReader
from city_data import CityData


def read_city_from_csv(file_path, city_name):
    years = []
    populations = []
    
    with open(file_path, 'r') as file:
        reader = DictReader(file)

        for row in reader:
            if row['City'] == city_name:
                years.append(int(row['Year']))
                populations.append(int(row['Population']))

    start_year = years[0]

    return CityData(city_name, start_year, populations)