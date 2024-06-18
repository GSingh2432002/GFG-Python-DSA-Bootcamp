# Anagram Search
char = 256
def aresame(ct,cp):
    for i in range(char):
        if ct[i] != cp[i]:
            return False
        return True
def ispresent(txt,pat):
    n = len(txt)
    m = len(pat)
    ct = [0] * char
    cp = [0] * char
    for i in range(m):
        ct[ord(txt[i])] += 1
        cp[ord(pat[i])] += 1
    for i in range(m,n):
        if aresame(ct,cp):
            return True
        ct[ord(txt[i])] += 1
        ct[ord(txt[i-m])] -= 1
    return False
txt = "geeksforgeeks"
pat = "frog"
print(ispresent(txt,pat))