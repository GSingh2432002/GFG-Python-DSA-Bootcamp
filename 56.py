# Two Pointer Approach
def isPair(arr,x):
    i = 0
    j = len(arr) - 1
    while i < j:
        if arr[i] + arr[j] == x:
            return True
        elif arr[i] + arr[j] < x:
            i = i + 1
        else:
            j = j - 1
    return False
arr = list(map(int, input("Enter a sorted array of integers separated by spaces: ").split()))
x = int(input("Enter the sum you are looking for: "))

if isPair(arr,x):
    print("There is a pair with the given sum.")
else:
    print("There is no pair with the given sum.")