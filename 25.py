# Who has the majority?
class Solution:
    def majorityWins(self, arr, n, x, y):
        """
        Parameters:
        arr (list): The list of elements.
        n (int): The number of elements in the list.
        x (int): The first element to compare.
        y (int): The second element to compare.
        
        Returns:
        int: The element that appears more frequently. If both appear the same number of times, returns the smaller element.
        """
        # Initialize counters for both elements
        count_x = 0
        count_y = 0
        
        # Iterate through the array to count occurrences of x and y
        for i in arr:
            if i == x:
                count_x += 1
            elif i == y:
                count_y += 1
        
        # Determine which element appears more frequently
        if count_x > count_y:
            return x
        elif count_y > count_x:
            return y
        else:
            # If both elements appear the same number of times, return the smaller element
            return min(x, y)

# Example usage
solution = Solution()
arr = [1, 2, 3, 2, 3, 3, 2, 1, 1]
n = len(arr)
x = 2
y = 3

result = solution.majorityWins(arr, n, x, y)
print("Element with more appearances:", result)