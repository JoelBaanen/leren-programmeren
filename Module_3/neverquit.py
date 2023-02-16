aantal = int
for x in range(aantal):
    vraag = input("?")
    if  vraag == "quit":
        print(aantal)
    else:
        aantal += 1
