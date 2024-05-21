# Majority Element
def findMajority(arr,n):
    res = 0
    count = 1
    # Find a candidate for majority element
    for i in range(1,n):
        if arr[res] == arr[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            res = i
            count = 1
    # Verify the candidate
    count = 0
    for i in range(0,n):
        if arr[res] == arr[i]:
            count += 1
    # If the candidate occurs more than n//2 times, return the candidate
    if count <= n//2:
        res = -1
    return res
arr = [2, 2, 1, 1, 1, 2, 2]
n = len(arr)
print(findMajority(arr, n))
    