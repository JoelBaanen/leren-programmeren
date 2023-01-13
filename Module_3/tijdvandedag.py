for x in range(24):
    if x <= 12:
        print(x,"am")
    elif x <= 24:
        x -= 12
        print(x,"pm")