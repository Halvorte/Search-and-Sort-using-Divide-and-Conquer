import csv

# Quick sort

# First we need the latitude values of the cities
def csv_reader():
    A = []
    with open("Cities file/worldcities.csv", encoding="utf8", newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            A.append(float(row['lat']))
    return A


# Getting the latitudes from cities
lat = csv_reader()
