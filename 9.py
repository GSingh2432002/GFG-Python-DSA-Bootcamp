# ALl divisor of a number in ascending order
def find_divisor(n):
    divisors = []
    
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if n // i != i:
                divisors.append(n // i)
    divisors.sort()
    return divisors

if __name__ == '__main__':
    num = int(input("Enter the number: "))
    divisors = find_divisor(num)
    print("All divisors of", num, "in ascending order are:", divisors)