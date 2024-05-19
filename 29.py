# Second largest element in a list
def getSecMax(l):
    if len(l) <= 1:
        return None
    lar = l[0]
    slar = None
    for x in l[1:] :
        if x > lar:
            slar = lar
            lar = x
        elif x != lar:
            if slar == None or slar < x:
                slar = x
    return slar
l = [32,66,90,88]
print(getSecMax(l))