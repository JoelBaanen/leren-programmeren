import random 

kleurmnm = ['oranje','blauw','groen','bruin']
leegzak= {}

vraag = int(input("hoeveel= "))

for i in range(vraag):
    k = random.randint(0, len(kleurmnm)-1)
    if kleurmnm[k] not in leegzak:
        leegzak.update({kleurmnm[k]: 1})
    else:
        i = leegzak.get(kleurmnm[k]) + 1
        leegzak.update({kleurmnm[k]: i})

print(leegzak)