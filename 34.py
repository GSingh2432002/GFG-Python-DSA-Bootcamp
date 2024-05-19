# Left rotate by d places
def Rotate(l,d):
    n = len(l)
    reverse(l,0,d-1)
    reverse(l,d,n-1)
    reverse(l,0,n-1)
    
def reverse(l,b,e):
        while b<e:
            l[b], l[e] = l[e], l[b]
            b = b+1
            e = e-1
user_input = input("Enter a list of elements separated by spaces: ")
num_list = list(map(int, user_input.split()))
d = int(input("Enter the number of places to rotate left: "))
Rotate(num_list, d)
print("List after left rotation by", d, "places:", num_list)