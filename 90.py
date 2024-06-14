# Intersection of two arrays
def intersection(arr1, m, arr2, n):
    us = set()
    for i in range(m):
        us.add(arr1[i])
    res = 0
    for i in range(n):
        if arr2[i] in us:
            res = res + 1
            us.remove(arr2[i])
    return res
arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 3, 5, 2]
m = len(arr1)
n = len(arr2)

print(intersection(arr1, m, arr2, n))