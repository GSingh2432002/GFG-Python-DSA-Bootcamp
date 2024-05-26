# Median of Two sorted Array
def getMed(a1,a2):
    n1,n2 = len(a1), len(a2)
    b1,e1 = 0,n1
    while(b1 <= e1):
        i1 = (b1 + e1) // 2
        i2 = (n1 + n2 + 1) // 2 - i1
        mnr1 = float("int") if i1 == n1 else a1[i1]
        mxl1 = float("-int") if i1 == 0 else a1[i1 - 1]
        mnr2 = a2[i2]
        mxl2 = a2[i2-1]
        if mxl1 <= mnr2 and mxl2 <= mnr1:
            if (n1 + n2) % 2 == 0:
                return (max(mxl1,mxl2) + min(mnr1,mnr2)) / 2
            else:
                return max(mxl1,mxl2)
        elif mxl1 > mnr2:
            e1 = i1 - 1
        else:
            b1 = i1 + 1