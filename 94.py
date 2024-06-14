# Subarray with given sum
def issubsum(arr, sum):
    s, curr = 0, 0
    for i in range(len(arr)):
        curr += arr[i]
        while(sum > curr):
            sum -= arr[s]
            s += 1
        if (curr == sum):
            return True
    return False