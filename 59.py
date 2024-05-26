# Allocate Minimum pages
def minPages(arr,K):
    n = len(arr)
    s = sum(arr)
    mx = max(arr)
    low,high = mx, sum
    res = 0
    while low <= high:
        mid =(low + high) // 2
        if(isFeasible(arr, K, mid)):
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res
def isFeasible(arr, K, ans):
    req, s = 1,0
    for i in range(n):
        if arr[i] > ans:
            req += 1
            s = arr[i]
        else:
            s += arr[i]
    return(req <=K)