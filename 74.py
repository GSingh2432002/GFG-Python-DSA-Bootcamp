# Minimum Difference in an array
def mindiff(arr):
    res = arr[0]    
    arr.sort()
    for i in range(1, len(arr)):
        for j in range(i):
            res = min(res,abs(arr[i]-arr[j]))
    print(res)
arr = [5,3,8]
mindiff(arr)
