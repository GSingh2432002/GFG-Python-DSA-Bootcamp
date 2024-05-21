# Subarray with given sum
def isSubSum(arr,sum):
    s, curr = 0, 0
    for e in range(len(arr)):
        curr += arr[e]
        while (curr> sum):
            curr -= arr[s]
            s += 1
        if(curr == sum):
            return True
    return False
arr = [1, 4, 20, 3, 10, 5]
sum = 33
print(isSubSum(arr, sum))