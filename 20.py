# Mean and Median of Array
class Solution:
    def median(self, A, N):
        """
        Finds the median of the array elements.
        
        Parameters:
        A (list): The list of elements.
        N (int): The number of elements in the list.
        
        Returns:
        int: The median of the array elements.
        """
        # Step 1: Sort the array
        A.sort()
        
        # Step 2: Check if the number of elements is even or odd
        if N % 2 == 0:
            # If even, the median is the average of the two middle elements
            median = (A[N//2 - 1] + A[N//2]) / 2
        else:
            # If odd, the median is the middle element
            median = A[N//2]
        
        # Step 3: Return the median as an integer
        return int(median)
    
    def mean(self, A, N):
        """
        Finds the mean of the array elements.
        
        Parameters:
        A (list): The list of elements.
        N (int): The number of elements in the list.
        
        Returns:
        int: The mean of the array elements.
        """
        # Step 1: Calculate the sum of the elements
        total_sum = sum(A)
        
        # Step 2: Calculate the mean
        mean = total_sum / N
        
        # Step 3: Return the mean as an integer
        return int(mean)

solution = Solution()
A = [10, 20, 30, 40, 50]
N = len(A)
print("Median:", solution.median(A, N))
print("Mean:", solution.mean(A, N))