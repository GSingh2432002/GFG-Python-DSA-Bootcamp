# Trapping rainwater
def getWater(arr,n):
    if n <= 2:
        return 0
    res=0
    lmax = [0]*n
    rmax = [0]*n
    
    lmax[0] = arr[0]
    for i in range(1,n):
        lmax[i] = max(arr[i], lmax[i-1])
        
    rmax[n-1] = arr[n-1]
    for i in range(n-2, -1, -1):
        rmax[i] = max(arr[i], rmax[i+1])
        
    for i in range(1,n-1):
        res = res + (min(lmax[i], rmax[i]) - arr[i])
    return res
user_input = input("Enter heights of buildings separated by spaces: ")
heights = list(map(int, user_input.split()))
water_trapped = getWater(heights, len(heights))
print("Total units of water trapped:", water_trapped)