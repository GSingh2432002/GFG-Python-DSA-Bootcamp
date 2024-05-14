# Palindrome number: if we read the number from right to left or left to right we get the same number.

def isPal(n): # defines a function named 'isPal' that takes one argument 'n'
    rev = 0 # This initializes a variable 'rev' to 0. This variable will store the reverse of the number 'n'
    temp = n # This line creates a temporary variable 'temp' and assigns it the value of 'n'. This variabl will be used for manipulation within the loop or function without affecting the original value of 'n'
    while temp != 0: # This initiate a while loop that continues until the value of 'temp' becomes 0
        lastdigit = temp % 10 #This calculates the last digit of 'temp' using the modulo operator '%'
        rev = rev * 10 + lastdigit # This line appends the last digit of 'temp' to the 'rev' variable, effectively reversing the number
        temp = temp // 10 # This line removes the last digit from 'temp' by performing integer division by 10. This effectively removes the last digit from the numebr.
    return rev == n # Once the while loop completes, the function returns 'true' if the reversed number 'rev' is equal to the original number 'n' indicating that 'n' is a palindrome.

if __name__ == '__main__': # This lines checks if the script is being run directly
    number = 4553 # This line assigns the number 4553 to the variable 'number'
    print(isPal(number)) # This line calls 'isPal' function with the 'number' as an argument and prints the result.
        