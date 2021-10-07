# MergeSort
# Start by reading the CSV file.

import csv

# Function to read csv
def csv_reader():
    A = []
    with open("Cities file/worldcities.csv", encoding="utf8", newline='') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            A.append(float(row['lat']))
    return A


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
    if len(array) > 1:

        left_arr = array[:len(array)//2]
        right_arr = array[len(array)//2:]

        # Recursion
        new_mergeSort(left_arr)
        new_mergeSort(right_arr)

        # Merge
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



print(csv_reader())

# Merge sort
lat = csv_reader()
#sortedLat = mergeSort(lat, 0, (len(lat)-1) )
#print(sortedLat)
array_test = [5,6,2,9,5,3,1,0,9,7]
#new_mergeSort(array_test)
#print(array_test)
new_mergeSort(lat)
print(lat)
