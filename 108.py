# Leftmost Repeating character
char = 256
def leftmost(st):
    visited = [False] * char
    res = -1
    for i in range(len(st) - 1, -1, -1):
        if (visited[ord(st[i])] == True):
            res = i
        else:
            visited[ord(st[i])] = True
    return res
st = "abccbd"
print(leftmost(st))