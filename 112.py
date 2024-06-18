# Naive Pattern Searching
def naivepat(txt, pat):
    m = len(pat)
    n = len(txt)
    for i in range(n-m+1):
        j = 0
        while j < m:
            if pat[j] != txt[i+j]:
                break
            j = j + 1
        if j == m:
            print(i)
txt = "ABCABCD"
pat = "ABCD"
naivepat(txt,pat)