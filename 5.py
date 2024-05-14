# Greatest Common Divisor
"""
Euclidean Algorithm:-
a=12, b=15
a=12, b=15-12 = 3
a=12-3 = 9, b=3
a=9-3 = 6, b=3
a=6-3 = 3, b=3
Therefore, both a and b is having the same result so we can return any value a or b
"""
    
def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a
if __name__ == '__main__':
    a = 12
    b = 15
    print("The GCD is: " + str(gcd(a,b)))