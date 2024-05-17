# Get Element At Index
def getByIndex(arr,n,index): # arr: the array from which we want to get an element.
                                # n: the number of elements in the array
                                # index: the index of the element we want to retrieve from the array.
    if index >= n: # This line checks if the index 'index' is out of the valid range, specifically if 'index' is greater than or equal to n
        return -1 # If it is, return -1
    else:
        return arr[index] # If it isn't, return the element at the index 'index' in the array 'arr'
arr = [10,20,30,40,50]       
n = len(arr)
index = 2
result = getByIndex(arr, n, index)
print(result)
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                
                                