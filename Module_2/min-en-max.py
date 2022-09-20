a = int(input("Welke getal is a?\n"))
b = int(input("Welke getal is b?\n"))

if a > b: 
    max = a
    min = b
    print("a is greater than b")
elif a < b:
    min = a
    max = b
    print("a is smaller than b")
if a == b:
    print("The values are equal")
else:
    print("The minimum is :", min)
    print("The maximum is :", max)


