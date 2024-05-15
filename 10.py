# Sieve of Eratosthenes
def sieve(n):
    if n <= 1:
        return
    isPrime = [True] * (n + 1) # isPrime: is the name of the list being initialized, [True]: this is a list containing a single element True, * (n + 1): This part repeats the [True] list n + 1 times creating a list with n + 1 elements all set to True.
    i = 2
    while i * i <= n: #Checks if the square of i is less than or equal to n
        if isPrime[i]: # Checks if i is still marked as prime
            for j in range(2 * i, n + 1, i): 
                # The loop marks the multiples of i as non-prime because any multiple of i greater than i itself cannot be a prime number.By starting at 2 * i, we skip i itself (which is prime if i hasn't been marked yet).
                
                # 2 * i: the starting point of the range. it is set 2 * i becoz we want to start marking multiples of i from the first multiple of i greater than i itself, n + 1: the endpoint of the range. it is set to n+1 to include n in the range since the range functions upper limit is exclusive, i: step size. it ensures that we are iterating over multiples of i.
                
                # for j in range(2 * p, n + 1, p): starts from 2 * p and marks every multiple of p as non-prime (False).
                isPrime[j] = False
        i += 1 # increments i to the next number
    for i in range(2, n + 1): # range(2, n+1) initializes a loop that iterates over the range of integer from 2 to n, isPrime[i]: this line checks if the current number i is marked as True in the isPrime list. If isPrime[i] is True it means that i has not been marked as a multiple of any smaller prime numbers and is therefore a prime number, print(i, end=""): this line prints the value of i and function specifies that the printed values should not be followed by a newline character.
        if isPrime[i]:
            print(i, " ", end="")
if __name__ == '__main__':
    n = 30
    sieve(n)