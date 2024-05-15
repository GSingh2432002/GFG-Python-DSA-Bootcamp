# Iterative Power
def power(x, n):
    res = 1  # Initialize result to 1, as any number to the power of 0 is 1
    while n > 0:
        if n % 2 != 0: # If n is odd, multiply the result by the current value of x
            res = res * x
        x = x * x # Square the base
        n = n // 2 # Divide n by 2, discarding the remainder
    return res # Return the power
if __name__ == '__main__':
    x = float(input("Enter the base: "))
    n = int(input("Enter the exponent: "))
    print("The result is", power(x, n))