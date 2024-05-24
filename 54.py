# Search in a sorted Rotated Array
def search(arr, n, x):
    low = 0 # Initialize the low pointer to the start of the array.
    high = n-1 # Initialize the high pointer to the end of the array.
    while low <= high: # Continue the loop until the search space is exhausted.
        mid = (low + high) // 2 # Calculate the middle index.
        if arr[mid] == x: # If the middle element is the target, return its index.
            return mid
        if arr[low] < arr[mid]: # Check if the left half is normally ordered.
            if arr[low] <= x < arr[mid]: # If the target is within the left half.
                high = mid -1 # Move the high pointer to search in the left half.
            else: # If the target is not within the left half.
                low = mid + 1 # Move the low pointer to search in the right half.
        else: # If the right half is normally ordered.
            if arr[mid] < x <= arr[high]: # If the target is within the right half.
                low = mid + 1 # Move the low pointer to search in the right half.
            else: # If the target is not within the right half.
                high = mid - 1 # Move the high pointer to search in the left half.
    return -1 # If the target is not found, return -1
arr = [4,5,6,7,0,1,2]
n = len(arr)
target = 0
position = search(arr,n,target)
print(f"Target {target} found at position {position}")