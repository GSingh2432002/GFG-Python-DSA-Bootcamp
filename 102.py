# More than n/k occurences
from collections import Counter

# Function to find the number of array
# elements with frequency more than n/k times
def printElements(arr, n, k):

    # Calculating n/k
    x = n//k

    # Counting frequency of every 
    # element using Counter
    mp = Counter(arr)
    
    # Traverse the map and print all
    # the elements with occurrence 
    # more than n/k times
    for it in mp:
        if mp[it] > x:
            print(it)


# Driver code
if __name__ == '__main__':
    arr = [1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1]
    n = len(arr)
    k = 4
    
    printElements(arr, n, k)