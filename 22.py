# Find Immediate Smaller than X
class Solution:
    def immediateSmaller(self, arr, n, x): # arr: The list of elements.
        # n: The number of elements in the list.
        # x: The target number.
        small = []  # Initialize an emptylist to store elements smaller than x
        for i in arr: # Iterate through each element in the array
            if i < x: # If the element is smaller than x
                small.append(i) # Append it to the list of smaller elements
        if small == []: # If there are no elements smaller than x
            return -1 # Return -1 indicating no immediate smaller element
        else:
            return max(small) # Return the maximum value from the list of smaller elements
solution = Solution()
arr = [4,5,2,10,8]
n = len(arr)
x = 3
result = solution.immediateSmaller(arr,n,x)
print("Immediate smaller elements:", result)