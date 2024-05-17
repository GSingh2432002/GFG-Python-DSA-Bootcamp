# Find immediate greater than X
class Solution:
    def immediateGreater(self, arr, n, x):
        """        
        Parameters:
        arr (list): The list of elements.
        n (int): The number of elements in the list.
        x (int): The target number.
        
        Returns:
        int: The smallest element greater than x, or inf if no such element exists.
        """
        # Initialize a variable to hold the smallest element greater than x
        immediate_greater = float('inf')
        
        # Iterate through the array elements
        for num in arr:
            # Check if the current element is greater than x and smaller than the current immediate_greater
            if num > x and num < immediate_greater:
                immediate_greater = num
        
        # If no element is greater than x, immediate_greater will still be inf
        if immediate_greater == float('inf'):
            return -1  # or return immediate_greater if you want to return inf explicitly
        else:
            return immediate_greater

# Example usage
solution = Solution()
arr = [4, 5, 2, 10, 8]
n = len(arr)
x = 5

result = solution.immediateGreater(arr, n, x)
print("Immediate greater element than", x, ":", result)