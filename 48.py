# Rope Cutting Problem
def maxPieces(n,a,b,c):
    if n == 0:
        return 0
    if n <= -1:
        return -1
    res = max(maxPieces(n-1, a, b, c),
              maxPieces(n-b, a, b, c),
              maxPieces(n-c, a, b, c))
    if res == -1:
        return -1
    return res + 1
n = 23
a = 11
b = 9
c = 12
print(maxPieces(n, a, b, c))