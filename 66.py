# Intersection of two sorted arrays
def union_array(arr1,arr2):
    m = len(arr1)
    n = len(arr2)
    i = 0
    j = 0
    prev = None
    while i<m and j<n:
        if arr1[i] < arr2[j]:
            if arr1[i] != prev:
                print(arr1[i], end=' ')
                prev = arr1[i]
            i += 1
        elif arr1[i] > arr2[j]:
            if arr2[j] != prev:
                print(arr2[j], end=' ')
                prev = arr2[j]
            j += 1
        else:
            if arr1[i] != prev:
                print(arr1[i], end=' ')
                prev = arr1[i]
            i += 1
            j += 1
    while i<m:
        if arr1[i] != prev:
            print(arr1[i], end=' ')
            prev = arr1[i]
        i += 1
    while j<n:
        if arr2[j] != prev:
            print(arr2[j], end=' ')
            prev = arr2[j]
        j += 1
if __name__ == '__main__':
    arr1 = [1,2,2,2,3]
    arr2 = [2,3,4,5]
    
    union_array(arr1, arr2)