# Array update at index
def updateArray(arr, n, idx, element): # arr: The array in which we want to update an element.
    # n (int): The total number of elements in the array.
    # idx (int): The index at which to update the element.
    # element: The new element to be placed at the specified index.
    if idx < 0 or idx >= n: # Check if the index is within the valid range
        print("Index out of range")
        return
    arr[idx] = element # update the element at the specified index
arr = [10,20,30,40,50]
n = len(arr)
idx = 3
element = 35
updateArray(arr,n,idx,element)
print(arr)