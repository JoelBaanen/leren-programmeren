from random import randint

kleur = ['oranje','blauw','groen','bruin']
vraag = int(input("hoeveel m&m's wil je"))
leegzak= []

for x in range(vraag):
    random = randint(0,3)
    random_num = kleur[random]
    leegzak.append(random_num)

print(leegzak)