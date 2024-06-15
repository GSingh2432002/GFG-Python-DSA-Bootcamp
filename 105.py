# Check for palindrome 
def palindrome(s):
    return s == s[::-1]
s = "malayalam"
ans = palindrome(s)

if ans:
    print("YES")
else:
    print("NO")