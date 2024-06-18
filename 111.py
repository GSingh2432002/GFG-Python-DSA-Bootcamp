# Pattern Searching in Python
txt = input("Enter the text:\n")
pat = input("Enter the pattern:\n")
pos = txt.find(pat)
while pos >= 0:
    print(pos)
    pos = txt.find(pat,pos+1)