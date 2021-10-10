import csv
import random

def csv_reader():
    A = []
    dicts = []
    with open("Cities file/worldcities.csv", encoding="utf8", newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:

            # Adding the lat and lng to a dictionary
            lat = float(row['lat'])
            lng = float(row['lng'])
            city = row['city']
            if row['country'] == 'Norway':
                dicts.append({'lat': lat, 'lng': lng, 'city': city})
                A.append(float(row['lat']))

    return A, dicts


def summ(freq, i, j):
    return sum(freq[i:j])

def optimal_binary_search_tree(sorted_list, frequency, n):
    return opt_cost(freq, 0, n-1)


def opt_cost(freq, i, j):
    if j < i:
        return
    if j == i:
        return freq[i]

    tsum = summ(freq, i, j)
    min = max

    for r in range(i, j + 1):
        cost = opt_cost(freq, i, r - 1) + opt_cost(freq, r + 1, j)
        if cost < min:
            cost = min
    return tsum + min,




lat, dicts = csv_reader()

#set frequencies
freq = []
for i in dicts:
    freq.append(random.randint(0,10))

print(len(lat))
print(len(freq))

print(dicts)
print(len(dicts))