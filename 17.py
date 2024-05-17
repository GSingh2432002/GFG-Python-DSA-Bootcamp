# Array insert at index
def insertAtIndex(arr, sizeOfArray, index, element): # arr: The array to which we want to add an element
    # sizeOfArray: The current number of elements in the array
    # index: The index at which tp insert the new element
    # element: The element to be inserted at the specified index
    if index < 0 or index > sizeOfArray: # Check if the index is within the valid range
        print("Index out of range")
        return
    arr.insert(index, element) # Insert the elements at the specified index
arr = [10,20,30,40,50]
sizeOfArray = len(arr)
index = 2
element = 25
insertAtIndex(arr, sizeOfArray, index, element)
print(arr)