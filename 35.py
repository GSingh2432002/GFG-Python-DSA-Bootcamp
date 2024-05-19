# Maximum Difference
def maxDiff(arr,n):
    res = arr[1] - arr[0]
    minval = arr[0]
    for j in range(1,n):
        res = max(res,arr[j] - minval)
        minval = min(arr[j],minval)
    return res
user_input = input("Enter a list of numbers separated by spaces: ")
num_list = list(map(int, user_input.split()))
result = maxDiff(num_list, len(num_list))
print("The maximum difference between any two elements where the larger element appears after the smaller element is:", result)