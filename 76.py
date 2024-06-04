# Sort an array with two types of element
def sort(arr):
    i,j = -1,len(arr)
    while True:
        i += 1
        while arr[i] < 0:
            i += 1
        j -= 1
        while arr[j] >= 0:
            j -= 1
        if i >= j:
            return
        arr[i], arr[j] = arr[j], arr[i]
    return arr
arr = [-12,18,-10,15]
print(sort(arr))