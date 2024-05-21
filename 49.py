# Subset of a given string
def Sub(str, curr, index):
    if index == len(str):
        print(curr, end='')
        return
    Sub(str, curr, index + 1)
    Sub(str, curr + str[index], index+1)
    
def generateSubsets(input):
    Sub(input, "", 0)
    
input = "abc"
generateSubsets(input)