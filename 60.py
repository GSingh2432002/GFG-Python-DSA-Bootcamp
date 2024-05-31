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

'''