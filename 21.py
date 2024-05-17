# Count Smaller than X
class Solution:
    def smallerThanX(self, arr, n, x):
        """
        Parameters:
        arr (list): The list of elements.
        n (int): The number of elements in the list.
        x (int): The target number.
        
        Returns:
        int: The count of elements smaller than x.
        """
        # Initialize a variable count to keep track of the number of elements smaller than x
        count = 0
        
        # Iterate through the array elements
        for num in arr:
            # If the current element is smaller than x, increment the count
            if num < x:
                count += 1
        
        # Return the count of elements smaller than x
        return count

# Example usage
solution = Solution()
arr = [10, 20, 30, 40, 50]
n = len(arr)
x = 55

result = solution.smallerThanX(arr, n, x)
print("Count of elements smaller than", x, ":", result)