# Pair with sum in unsorted array
def printPairs(arr, arr_size, sum):
    hashmap = {}
    for i in range(0, arr_size):
        temp = sum-arr[i]
        if(temp in hashmap):
            print('Yes')
            return
        hashmap[arr[i]] = i
    print("No")