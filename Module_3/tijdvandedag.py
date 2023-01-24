
for x in range(25):
    if 1 <= x <= 12:
        print(x,"am")
    elif x >= 12:
        x -= 12
        print(x,"pm")