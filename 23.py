# Count Elements greater than X
class Solution:
    def greaterThanX(self, arr, n, x):
        # arr: the list of elements
        # n: the number of elements in the list
        # x: the target number
        c = 0
        for i in arr:
            if i > x:
                c += 1
        return c
solution = Solution()
arr = [4,5,2,10,8]
n = len(arr)
x = 5
result = solution.greaterThanX(arr,n,x)
print(x, ":", result)