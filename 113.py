# Improved Naive Pattern Searching for Distinct
def distpatsearch(txt,pat):
    m = len(pat)
    n = len(txt)
    i = 0
    while i <= (n-m):
        for j in range(m):
            if pat[j] != txt[i+j]:
                break
            j += 1
            if j == m:
                print(i, end = "")
                i += m
            if j == 0:
                i += 1
            else:
                i += j
txt = "ABCABCD"
pat = "ABCD"

distpatsearch(txt, pat)