# Triplet in a Sorted Array
def isPair(arr, x, si):
    i = si
    j = len(arr) - 1
    while i < j:
        if arr[i] + arr[j] == x:
            return True
        elif arr[i] + arr[j] < x:
            i = i + 1
        else:
            j = j - 1
    return False
def isTriplet(arr,x):
    for i in range(len(arr) - 2):
        if(isPair(arr, x-arr[i], i+1)):
            return True
    return False
arr = list(map(int, input("Enter a sorted array of integers separated by spaces: ").split()))
x = int(input("Enter the sum you are looking for: "))

if isTriplet(arr,x):
    print("There is a triplet with the given sum")
else:
    print("There is no triplet with the given sum")