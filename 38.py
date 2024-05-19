# Maximum Sum subarray
def maxSum(arr,n):
    res = arr[0]
    maxEnding = arr[0]
    for i in range(1,n):
        maxEnding = max(maxEnding + arr[i], arr[i])
        res = max(maxEnding, res)
    return res
user_input = input("Enter a list of numbers separated by spaces: ")
num_list = list(map(int, user_input.split()))
result = maxSum(num_list, len(num_list))
print("Maximum sum of a subarray is:", result)