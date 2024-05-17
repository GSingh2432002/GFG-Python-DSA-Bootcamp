# Separate Even and Odd
def getEvenOdd(l):
    even = []
    odd = []
    for x in l:
        if x % 2 == 0:
            even.append(x)
        else:
            odd.append(x)
    return even, odd # This line returns a tuple containing the even and odd lists. The even list contains all even numbers from the input list l and the odd lust contains all odd numbers.
l = [10, 12, 13, 17, 18] # This line creates a list named l containing the numbers 10,12,13,17,18
even, odd = getEvenOdd(l) # This line calls the getEvenOdd function with the list l as an argument. The function returns two lists (even & odd), which are assigned to the variables even and odd.
print(even)
print(odd)