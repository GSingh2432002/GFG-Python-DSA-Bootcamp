# Union of Two Sorted Array
def Union(a,b,n,m):
    i = 0
    j = 0
    while(i<len(a) and j<len(b)):
        if (i>0 and a[i] == a[i-1]):
            i = i+1
        elif(j>0 and b[j]==b[j-1]):
            j = j+1
        elif(a[i] < b[j]):
            print(a[i],end=" ")
            i = i+1
        elif(a[i] > b[j]):
            print(b[i], end="")
        else:
            print(a[i], end=" ")
            i = i+1
            j = j+1
    while(i<len(a)):
        if(i>0 and a[i]!=a[i-1]):
            print(a[i], end="")
        i = i+1
    while(j<len(b)):
        if(j>0 and b[j]!=b[j-1]):
            print(b[j], end="")
        j = j+1