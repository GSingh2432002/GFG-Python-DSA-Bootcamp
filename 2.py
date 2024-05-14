# Count Digits
x =int(input("Enter x: "))
res =0 
while x > 0:
    x = x // 10 #Keep dividing the number by 10 the last digit gets eliminated from the original number.
    res = res + 1
print("Count of digits are: " + str(res))