import csv


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
            city = row['city']
            dicts.append({'lat': lat, 'lng': lng, 'city': city})

    return A, dicts


# function binary searching for target in a sorted list
def binary_search(lat, target):
    pivot = len(lat)//2

    if len(lat) == 1 and lat[pivot] != target:
        print('false')
        return False

    if lat[pivot] == target:
        print(f'Found target: {target}')
        return True
    elif lat[pivot] > target:
        return binary_search(lat[:pivot], target)
    else:
        return binary_search(lat[pivot:], target)


def new_mergeSort(array):
    #global merge_count
    if len(array) > 1:

        left_arr = array[:len(array)//2]
        right_arr = array[len(array)//2:]

        # Recursion
        new_mergeSort(left_arr)
        new_mergeSort(right_arr)

        # Merge
        # count number of merges necessary
        #merge_count += 1
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

def find_city(target, dictionaries):
    for i in dictionaries:
        city_lat = i['lat']
        city_name = i['city']
        if target == city_lat:
            print(city_name)



# Getting the lat of the cities
lat, dictionaries = csv_reader()
#print(f'Len lat: {len(lat)}')

#print(dictionaries)


# Sorted latitudes
# Can use both sorting methods from last two problems.

# Sorting using mergesort
new_mergeSort(lat)
#print(f'After sort:')
#print(lat)

# Setting target, and getting city name if target is found
target = 40.3635
if binary_search(lat, target) is True:
    print('City:')
    find_city(target, dictionaries)



