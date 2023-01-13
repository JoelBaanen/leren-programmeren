#Joel Baanennul
#Pizza calculator
from ast import Try
prijs_pizza_large = 12
prijs_pizza_medium = 10
prijs_pizza_small = 8
aantal_large = 0
aantal_medium = 0
aantal_small = 0
try:
    aantal_large = int(input("Hoeveel large pizzas wil je?"))
except:
    print("Jij heb iets niet goed ingetypt")    
try:
    aantal_medium = int(input("Hoeveel medium pizzas wil je?"))
except:
    print("Jij heb iets niet goed ingetypt")    
try:
    aantal_small = int(input("Hoeveel small pizzas wil je?")) 
except:
    print("Jij heb iets niet goed ingetypt")

prijs_large = aantal_large * prijs_pizza_large
prijs_medium = aantal_medium * prijs_pizza_medium
prijs_small = aantal_small * prijs_pizza_small

totaal_prijs = prijs_large + prijs_medium + prijs_small

print("-----------------------------------------")
print("| Prijs : €", totaal_prijs)
if prijs_small > 0:    
    print("| Voor : ", aantal_small,"kleine pizzas;")
if prijs_medium > 0:    
    print("| Voor : ", aantal_medium,"medium pizzas;")
if prijs_large > 0:    
    print("| Voor : ", aantal_large,"large pizzas;")
print("-----------------------------------------")