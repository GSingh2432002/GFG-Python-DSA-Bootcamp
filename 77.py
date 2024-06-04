# Sort an array with three types of elements
temp = []
def sortarr(arr):
    temp = []
    for x in arr:
        if x == 0:
            temp.append(x)
    for x in arr:
        if x == 1:
            temp.append(x)
    for x in arr:
        if x == 2:
            temp.append(x)
    for i in range(len(arr)):
        arr[i] = temp[i]
    return temp
arr = [0,1,1,2,0,1]
A = sortarr(arr)
print(A)