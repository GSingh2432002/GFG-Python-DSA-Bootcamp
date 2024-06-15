# Check for Anagram
s1 = input("Enter a string:\n")
s2 = input("Enter a string:\n")

def anagram(s1,s2):
    if len(s1) != len(s2):
        return False
    count = [0]*256
    for i in range(len(s1)):
        count[ord(s1[i])] += 1
        count[ord(s2[i])] -= 1
    for x in count:
        if x != 0:
            return False
    return True