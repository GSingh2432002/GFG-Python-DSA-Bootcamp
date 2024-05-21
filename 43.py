# Sliding Window Technique
def KMaxSum(arr,K):
    # Initial sum of the first window of size K
    curr = 0
    for i in range(K):
        curr += arr[i]
    res = curr
    # Slide the window from start to end of the array
    for i in range(K, len(arr)):
        curr = curr + arr[i] - arr[i-K]
        res = max(res, curr)
    return res
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
K = 3
print(KMaxSum(arr, K)) 