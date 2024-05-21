# Equilibrium Point
def ePoint(arr):
    rs = sum(arr)
    ls = 0 
    for i in range (len(arr)):
        rs -= arr[i]
        if(ls == rs):
            return True
        ls += arr[i]
    return False
print(ePoint([1, 3, 5, 2, 2]))
print(ePoint([1, 2, 3, 4, 5]))
print(ePoint([2, 4, 2]))
print(ePoint([1, 1, 1, 1, 1, 1]))