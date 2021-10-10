# MergeSort
# Start by reading the CSV file.

import csv
import random
import math
from math import radians, cos, sin, asin, sqrt

merge_count = 0

# Function to read csv
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

# MergeSort function
def mergeSort(A, p, r):
    # A - list
    # p - element p. first element
    # r - element r. last element
    if p < r:
        q = (p + r) // 2

        mergeSort(A, p, q)
        mergeSort(A, q+1, r)
    #A = A1 + A2
    merge(A, p, q, r)


# Merge function
def merge(A, p, q, r):
    sortLi = []
    i = j = k = 0
    while i < p + q and j < q + r:
        print("yo")

def new_mergeSort(array):
    global merge_count
    if len(array) > 1:

        left_arr = array[:len(array)//2]
        right_arr = array[len(array)//2:]

        # Recursion
        new_mergeSort(left_arr)
        new_mergeSort(right_arr)

        # Merge
        # count number of merges necessary
        merge_count += 1
        i = 0
        j = 0
        k = 0
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                array[k] = left_arr[i]
                i += 1
            else:
                array[k] = right_arr[j]
                j += 1
            k += 1

        while i < len(left_arr):
            array[k] = left_arr[i]
            i += 1
            k += 1

        while j < len(right_arr):
            array[k] = right_arr[j]
            j += 1
            k += 1

'''
    q = len(array)//2
    left = array[:q]
    right = array[q:]

    left = new_mergeSort(left)

    right = new_mergeSort(right)

    return new_merge(left, right, array)
'''

def new_merge(left, right, array):
    len_left = len(left)
    len_right = len(right)
    i = j = k = 0

    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1

        else:
            array[k] = right[j]
            j += 1

        k += 1

    print(array)

def sort_by_distance(dict):
    distances = []

    for i in dict:
        data = i['distance']
        # i.get('distance', dist)
        distances.append(data)

    # Sorting the distances.
    new_mergeSort(distances)
    print(distances)

    sorted_dicts = []

    for j in distances:
        for k in dict:
            if j == k['distance']:
                sorted_dicts.append(k)

    return sorted_dicts

#print(csv_reader())
#print()

# Merge sort

# getting
lat, dict = csv_reader()
print(f'Distance: {dict}')

#print(f'before shuffle: {lat}')
random.shuffle(lat)
#print(f'After shuffle: {lat}')
#print(lat)
#sortedLat = mergeSort(lat, 0, (len(lat)-1) )
#print(sortedLat)
array_test = [5,6,2,9,5,3,1,0,9,7]

sorted_dictionaries = sort_by_distance(dict)



print(f'Sorted dicts:')
for k in sorted_dictionaries:
    print(k)
print(f'number of sorted dicts: {len(sorted_dictionaries)}')

print(f'Number of merges: {merge_count}')
