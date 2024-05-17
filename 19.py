# Array Delete and Shift
def deleteFromArray(arr,n,index):
    # arr (list): The array from which we want to delete an element.
    # n (int): The total number of elements in the array (not used in this implementation).
    # index (int): The index of the element to be deleted.
    if index < 0 or index >= len(arr):
        return "Index out of bound"
    else:
        for i in range(index, len(arr) - 1): # This else block executes if the index is valid.
            # A for loop iterates from the index to the second-to-last element of the array.
            # Each element at position i is replaced by the element at position i+1. This shifts all elements after the index one position to the left
            arr[i] = arr[i+1]
        arr[-1] = 0 # After shifting elements the last element of the array is set to 0 to simulate deletion. This assumes that the array was initially full and that we want to remove the last element after shifting.
        return arr # Returns the updated array after the deletion operation.
arr = [10,20,30,40,50]
n = len(arr)
index = 2
result = deleteFromArray(arr,n,index)
print(result)