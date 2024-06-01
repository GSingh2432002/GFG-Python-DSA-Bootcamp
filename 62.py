# Selection Sort
def selection_sort(l):
    n = len(l)
    for i in range(n-1):
        min_ind = i
        # From i+1 till n
        for j in range(i+1,n):
            if l[j] < l[min_ind]:
                min_ind = j
        l[min_ind], l[i] = l[i], l[min_ind]
l = [10,5,8,20,2,18]
selection_sort(l)
print(*l)