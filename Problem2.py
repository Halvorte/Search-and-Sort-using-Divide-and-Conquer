import csv
import random
import math
from math import radians, cos, sin, asin, sqrt

comparison_count = 0

# Quick sort

# First we need the latitude values of the cities
def csv_reader():
    A = []
    B = []
    dicts = []
    with open("Cities file/worldcities.csv", encoding="utf8", newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            A.append(float(row['lat']))
            B.append(float(row['lng']))

            # Adding the lat and lng to a dictionary
            lat = float(row['lat'])
            lng = float(row['lng'])
            distance = distance_haversine(lat, lng)
            dicts.append({'lat': lat, 'lng': lng, 'distance': distance})

    return A, dicts


# Function to calculate distance between two points on earth
def distance_haversine(lat, lng):
    lat1 = lat
    lon1 = lng
    lat2 = 0.0
    lon2 = 0.0

    """
    Calculate the great circle distance in kilometers between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles. Determines return value units.
    distance = c * r
    return distance


# Function for the quick sorting
def sort(array):

    # Function to do the quick sorting
    def quick_sort(array, low, high):
        global comparison_count
        # Check that high (len(array)-1) is bigger than low (0)
        if high <= low:
            return

        # Choose a random pivot from the range low to high
        piv = random.randint(low, high)

        # Move pivot to the front of the array. Put the pivot to the first position in the array
        tmp = array[low]
        array[low] = array[piv]
        array[piv] = tmp

        # Partion
        j = low
        for i in range(low+1, high+1):
            # Is the current element in the array smaller than the first element, which is the pivot.
            # Also add one to the comparison count
            comparison_count += 1
            if array[i] < array[low]:

                j += 1

                # swap positions of the current element i smaller than the pivot with the position of j.
                tmp1 = array[j]
                array[j] = array[i]
                array[i] = tmp1

        # Place pivot in correct position
        tmp2 = array[j]
        array[j] = array[low]
        array[low] = tmp2

        # Sort left and right
        quick_sort(array, low, j - 1)
        quick_sort(array, j + 1, high)

    # Check if the array is empty or only has one element.
    if array is None or len(array) < 2:
        return

    # Sort the array
    quick_sort(array, 0, len(array) - 1)


    '''
    if len(array) > 1:
        # Choosing a random pivot
        #rand = random.randint(0, len(array) - 1)
        #Math.random =
        #i = array[rand]
        #i = random.choice(array)
        #i = array[-1]
        i = rand(array)

        #while len(array) >= 1:
        for j in array:
            if j < i:
                A1.append(j)
            else:
                A2.append(j)

        quick_sort(A1)
        quick_sort(A2)
        print(f'a1 + a2 : {A1 + A2}')
        return A1 + A2
    else:
        return array
    '''



# quick sort using the last element in the array as the last element in the array
def new_quick_sort(array, low, high):
    if len(array) == 1:
        return array
    if low < high:
        piv = pivot(array, low, high)

        new_quick_sort(array, low, piv-1)
        new_quick_sort(array, piv+1, high)


# Find pivot for the new_quick_sort function
def pivot(array, low, high):
    piv = array[high]
    #piv = random.choice(array)
    item = low - 1

    for i in range(low, high):
        if array[i] <= piv:
            item = item + 1
            tmp = array[item]
            array[item] = array[i]
            array[i] = tmp

    tmp = array[item + 1]
    array[item + 1] = array[high]
    array[high] = tmp

    return item + 1


def sort_by_distance(dict):
    distances = []

    for i in dict:
        data = i['distance']
        # i.get('distance', dist)
        distances.append(data)

    # Sorting the distances.
    sort(distances)
    print(distances)

    sorted_dicts = []

    for j in distances:
        for k in dict:
            if j == k['distance']:
                sorted_dicts.append(k)

    return sorted_dicts



array_test = [5,6,2,9,5,3,1,0,9,7]

# Getting the latitudes from cities
lat, dictionaries = csv_reader()
print(lat)
#sorted = quick_sort(array_test)
#print(f'sorted: {sorted}')
#print(quick_sort(lat))

#new_quick_sort(lat, 0, len(lat)-1)
#print(lat)

#new_quick_sort(array_test, 0, len(array_test)-1)
#print(array_test)
sort(lat)
#print(lat)
print(f'Comparison count: {comparison_count}')
#print(dictionaries)

sorted_dictionaries = sort_by_distance(dictionaries)
print('Sorted dictionaries: ')
for k in sorted_dictionaries:
    print(k)
#print(sorted_dictionaries)
