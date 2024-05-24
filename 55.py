# Find a Peak element
def getPeak(arr,n):
    low = 0 # Initialize the low pointer to the start of the array.
    high = n - 1 # Initialize the high pointer to the end of the array.
    while low <= high: # Continue the loop until the search space is exhausted.
        mid = (low + high) // 2 # Calculate the middle index of the current search space.
        
        # Check if the middle element is a peak:
        # 1. If mid is the first element or the previous element is less than or equal to mid.
        # 2. If mid is the last element or the next element is less than or equal to mid.
        if((mid == 0 or arr[mid-1] <= arr[mid]) and (mid==n-1 or arr[mid+1] <= arr[mid])):
            return mid # If both condition are true, mid is a peak element. Return its index.
        
        # If the previous element is greater than the middle element, there must be a peak in the left half.
        if mid > 0 and arr[mid-1] >= arr[mid]:
            high = mid - 1 # Move the high pointer to the left of mid.
        
        # Otherwise, there must be a peak in the right half.
        else:
            low = mid + 1 # Move the low pointer to the right of mid.
    return -1 # If no peak is found, which theoretically shouldn't happen, return -1.
arr = [1,3,20,4,1,0]
n = len(arr)
peak_index = getPeak(arr,n)
print(f"Peak element found at index {peak_index}, value: {arr[peak_index]}")