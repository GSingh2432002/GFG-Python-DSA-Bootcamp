# Subset sum problem
def Subsets(arr,n,sum):
    if n==0:
        return 1 if sum==0 else 0
    return Subsets(arr, n-1, sum) + Subsets(arr, n-1, sum-arr[n-1])