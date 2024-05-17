# Max and Min in Array
def maximumElement(arr,n):
    #return required result
    
    #code here
    max=arr[0]
    for i in range(len(arr)):
        if arr[i]>max:
            max=arr[i]
    return max            



def minimumElement(arr,n):
    #return required result
    
    #code here
    min=arr[n-1]
    for i in range(0,n):
        if arr[i]<min:
            min=arr[i]

    return min

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
n = len(arr)

print("Maximum Element:", maximumElement(arr, n))  # Output: 9
print("Minimum Element:", minimumElement(arr, n))