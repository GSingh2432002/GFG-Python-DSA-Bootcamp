# Check if string is rotated
def rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    temp = s1 + s2
    return temp.find(s2) != -1
s1 = "ABCD"
s2 = "CDBA"
print(rotation(s1, s2))