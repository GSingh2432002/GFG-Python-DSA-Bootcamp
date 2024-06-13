# Dictionary in Python
d = {110: 'abc', 101: 'xyz', 105: 'pqr', 106: 'bcd'}

d[101] = 'wxy'

print(len(d))

print(d)

print('returning and removing 105', d.pop(105))

print('after removing 105', d)

del d[106]

print(d)

d[108] = 'cde'

print('returning and removing last inserted', d.popitem())