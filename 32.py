# Remove duplicates from a sorted array
def remdup(arr,n):
    res = 1
    for i in range(1,n):
        if(arr[res-1] != arr[i]):
            arr[res] = arr[i]
            res += 1
    return res
user_input = input("Enter a sorted list of numbers ")
num_list = list(map(int, user_input.split()))
new_length = remdup(num_list)
unique_list = num_list[:new_length]
print("The list after removing duplicates: {unique_list}")
print("The length of the list after removing duplicates: {new_length}")