# Prime Factorization
def prime_factors(n):
    factors = []
    divisor = 2
    
    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1
    
    return factors

if __name__ == '__main__':
    num = int(input("Enter the number"))
    print("Prime factors of", num, "are:", prime_factors(num))