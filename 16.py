# Array insert at end
def insertAtEnd(arr, sizeOfArray, element): # arr: The array to which we want to add an element
    # sizeOfArray: The current number of elements in the array
    # element: The element to be inserted at the end of the array.
    if sizeOfArray < len(arr): # Ensure we do not exceed the predefined size of the array
        arr[sizeOfArray] = element # Insert element at the first empty position
    else:
        arr.append(element) # Fallback to append in case the size is already at the limit
arr = [10,20,30,40,50]
sizeOfArray = 5
element = 60
insertAtEnd(arr, sizeOfArray, element)
print(arr)