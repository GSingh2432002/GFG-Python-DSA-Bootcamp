# LCM of two numbers
# Formula for finding LCM = a * b = gcd(a, b) * lcm(a, b)

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)
if __name__ == '__main__':
    a = 4
    b = 6
    print(lcm(a,b))
