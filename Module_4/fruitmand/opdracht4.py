from fruitmand import fruitmand
import random
aantal = int(input("Hoeveel fruit wil je?"))

for y in range (aantal):
    fruit_choice = random.choice(fruitmand)
    print(fruit_choice['name'])