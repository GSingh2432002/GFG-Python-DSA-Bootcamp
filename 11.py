# Computing Power
def power(x, n):
    if n==0:
        return 1
    temp = power(x, n//2)
    temp = temp * temp
    if(n % 2 == 0):
        return temp
    else:
        return temp * x
if __name__ == '__main__':
    x = float(input("Enter the base (x): "))
    n = int(input("Enter the exponent (n): "))
    print("The result is: ", power(x, n))
    
'''
def power(x, n): This line defines a function named power that takes two parameters: x (the base) and n (the exponent).

if n == 0:
    return 1
Checks if the exponent n is 0. If it is, the function returns 1 because any number raised to the power of 0 is 1. This is the base case for the recursion.

Recursive Call
temp = power(x, n // 2)
Recursively calls the power function with the base x and half the exponent n (using integer division n // 2). The result of this recursive call is stored in the variable temp.

Squaring the result:
temp = temp * temp
Squares the result of the recursive call (temp). This is because x^n=(x^n/2)^2

Handling Odd Exponent:
if n % 2 == 0:
    return temp
else:
    return temp * x
checks if the original exponents n is even or odd using the modulus operator(n%2)
if n is even it returns temp becoz x^n = x^n/2^2
if n is odd it multiplies temp by x and returns the result becoz x^n = x * (x^(n-1)/2^2)
'''