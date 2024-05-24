# Search in an Infinite Sized Array
def bsearch(arr, low, high, x):
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1 
def search(arr, x):
    if arr[0] == x:
        return 0
    i = 1
    # exponential search to find the range
    while arr[i] < x:
        i = i * 2
    # If we've found arr[i] == x
    if i < len(arr) and arr[i] == x:
        return i
    # Binary search within the identified range
    return bsearch(arr, i//2 + 1, i-1, x)
arr = [i for i in range(1, 1000000)]
target = 123456
position = search(arr, target)
print(f"Target {target} found at position {position}")