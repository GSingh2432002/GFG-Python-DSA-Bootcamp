# Check for Palindrome permutation
No_Of_Chars = 256
def canFormPalindrome(st):
    count = [0] * (No_Of_Chars)
    for i in range(0, len(st)):
        count[ord(st[i])] = count[ord(st[i])] + 1
        odd = 0
        for i in range(0, No_Of_Chars):
            if (count[i] & 1):
                odd = odd + 1
            if (odd > 1):
                return False
    return True