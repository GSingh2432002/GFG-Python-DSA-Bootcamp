# Set in Python
s = {10, 20}
s.add(30)
print(s)

s.add(30)
print(s)

s.update([40,50])
print(s)

s.update([60,70], [80,90])
print(s)


t = {10, 20, 30, 40}
t.discard(30)
print(t)

t.remove(20)
print(t)

t.clear()
print(t)

t.add(50)
del t

p1 = {2,4,6,8}
p2 = {3,6,9}

print('union', p1 | p2)
print(p1.union(p2))

print('intersecton', p1 & p2)
print(p1.intersection(p2))

print('present in s1, but not present in s2', p1 - p2)
print(p1.difference(p2))

print('symmetric differences, not present in both', p1 ^ p2)

s1 = {2,4,6,8}
s2 = {4,8}

print('disjoint sets:', s1.isdisjoint(s2))

print('isSubset:', s1 <= s2)
print(s1.issubset(s2))

print('proper set:', s1 < s2)

print('s1 is superset of s2:', s1 >= s2)
print(s1.issuperset(s2))

print('s1 is proper superset of s2:', s1 > s2)