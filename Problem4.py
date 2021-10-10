import csv
import random
import sys

# Define class for nodes
class Node:
    def __init__(self, key, freq):
        self.key = key
        self.freq = freq

    def __str__(self):
        return f'Node(key={self.key}, freq={self.freq})'

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



def optimal_binary_search_tree(nodes):

    # Sorts the nodes by key
    nodes.sort(key=lambda node: node.key)
    n = len(nodes)

    keys = []
    freqs = []
    for i in range(n):
        keys.append(nodes[i].key)
        freqs.append(nodes[i].freq)


    # Creating 2d array that stores the tree cost
    dp = [[freqs[i] if i == j else 0 for j in range(n)]for i in range(n)]

    # sum[i][j] stores the sum of key frequencies
    sum = [[i if i == j else 0 for j in range(n)]for i in range(n)]

    # Stores tree roots that will be used to construct the binary search tree
    root = [[i if i == j else 0 for j in range(n)]for i in range(n)]


    # j is interval length
    for j in range(2, n + 1):
        for k in range(n - j + 1):
            l = k + j - 1

            # sys.maxsize makes it "infinite"
            dp[k][l] = sys.maxsize
            sum[k][l] = sum[k][l - 1] + freqs[l]


            for r in range(root[k][l - 1], root[k + 1][l] + 1):
                # Optimal cost for left subtree
                left = dp[k][r - 1] if r != k else 0
                # Optimal cost for right subtree
                right = dp[r + 1][l] if r != l else 0

                cost = left + sum[k][l] + right


                if dp[k][l] > cost:
                    dp[k][l] = cost
                    root[k][l] = r

    print('Binary search tree nodes:')
    for node in nodes:
        print(node)

    print(f'Cost of optimal tree is {dp[0][n - 1]}.')

    # Function to print binary search tree
    print_bst(root, keys, 0, n - 1, -1, False)


# Function to print bst
def print_bst(root, key, i, j, parent, is_left):
    if i > j or i < 0 or j > len(root) - 1:
        return

    node = root[i][j]
    # Root does not have parent
    if parent == -1:
        print(f'{key[node]} is the root of the tree')
    elif is_left:
        print(f'{key[node]} is the left child of key {parent}.')
    else:
        print(f'{key[node]} is the right child of key {parent}.')

    print_bst(root, key, i, node - 1, key[node], True)
    print_bst(root, key, node + 1, j, key[node], False)




lat, dicts = csv_reader()

#set frequencies
freq = []
for m in dicts:
    freq.append(random.randint(0,10))


# Example keys and frequencies
ex_keys = [1, 2, 3, 4, 5]
ex_freq = [.213, .020, .547, .100, .120]
n = 5

# Create the nodes needed
nodes = []
for q in range(len(lat)):
    node = Node(lat[q], freq[q])
    nodes.append(node)
    '''
for q in range(len(ex_keys)):
    node = Node(ex_keys[q], ex_freq[q])
    nodes.append(node)
    '''

# Takes sorted by keys nodes.
optimal_binary_search_tree(nodes)


#print(len(lat))
#print(len(freq))

#print(dicts)
#print(len(dicts))