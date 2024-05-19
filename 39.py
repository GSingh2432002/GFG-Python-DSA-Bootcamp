# Longest Even Odd Subarray
def maxEvenOdd(arr,n):
    res =1 
    curr = 1
    for i in range(1,n):
        if(arr[i]%2 == 0 and arr[i-1]%2 != 0)\
            or (arr[i]%2 != 0 and arr[i-1]%2 == 0):
                curr += 1
                res = max(res, curr)
        else:
            curr = 1
    return res
user_input = input("Enter a list of numbers separated by spaces: ")
num_list = list(map(int, user_input.split()))
result = maxEvenOdd(num_list, len(num_list))
print("Length of the longest subarray with alternating even and odd elements is:", result)