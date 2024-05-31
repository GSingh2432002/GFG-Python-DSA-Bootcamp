# List Sort
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
def myFun(p):
    return p.x
l = [Point(1,15), Point(10,5), Point(3,8)]
l.sort(key=myFun)

for i in l:
    print(i.x, i.y)
    
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
This defines a 'Point' class with an '__init__' method that initializes 'Point' objects with two attributes: 'x' and 'y'. When a 'Point' object is created, the '__init__' method is called to set the values of 'x' and 'y'.

def myFun(p):
    return p.x
This defines a function 'myFun' that takes a 'Point' object 'p' as an argument and return its 'x' attribute. This function will be used as a key for sorting.

l = [Point(1, 15), Point(10, 5), Point(3, 8)]
This creates a list 'l' that contains three 'Point' objects. Each 'Point' object is initialized with specific 'x' and 'y' values: (1,15), (10,5), (3,8).

l.sort(key=myFun)
This sorts the list 'l' in place using the 'sort' method. The 'key' parameter specifies a function to be called on each list element prior to making comparisons. Here 'myFun' is used as the key function, which means the list will be sorted based on the 'x' attribute of each 'Point' object.
1. The 'sort' method goes through the list and calls 'myFun' on each 'Point' object to get the 'x' value.
2. It then sorts the 'Point' objects in ascending order based on these 'x' values.

for i in l:
    print(i.x, i.y)
This loop iterates over each "Point" object in the sorted list 'l'. For each 'Point' object 'i', it prints the 'x' and 'y' attributes.

1. Creating the list:
a. 'Point(1,15)' creates a 'Point' object with 'x=1' and 'y=15'.
b. 'Point(10,5)' creates a 'Point' object with 'x=10' and 'y=5'.
c. 'Point(3,8)' creates a 'Point' object with 'x=3' and 'y=8'.
These objects are added to list 'l'.

2. Sorting the List:
a. The 'sort' method calls 'myFun' on each 'Point' object to get the 'x' value:
i. 'myFun(Point(1,15))' returns '1'.
ii. 'myFun(Point(10,5))' returns '10'.
iii. 'myFun(Point(3,8))' returns '3'.
b. The list is sorted based on these 'x' values: '[1,10,3]' becomes '[1,3,10]'.
c. The sorted list is: '[Point(1,15), Point(3,8), Point(10,5)]'

3. Printing the Sorted List:
a. The loop iterates over the sorted list: 
i. 'Point(1,15)' it prints '1,15'.
ii. 'Point(3,8)' it prints '3,8'.
iii. 'Point(10,5)' it prints '10,5'.
'''