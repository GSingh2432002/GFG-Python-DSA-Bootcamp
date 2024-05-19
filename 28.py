# Largest Element in a list
def getMax(l):
    if not l:
        return None
    else:
        res = l[0]
        for i in range(1, len(l)):
            if l[i] > res:
                res = l[i]
    return res
l = [34,21,88,90,4]
print(getMax(l))