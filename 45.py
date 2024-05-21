# Prefix Sum Technique
arr = [2,8,3,9,6,5,4]
n = len(arr)
psum = [None] * n
psum[0] = arr[0]
for i in range (1,n):
    psum[i] = psum[i-1] + arr[i]
    
def getSum(l,r):
    if l == 0:
        return psum[r]
    else:
        return psum[r] - psum[l-1]
print(getSum(0, 2))
print(getSum(1, 3))  
print(getSum(2, 5))  
print(getSum(0, 6))