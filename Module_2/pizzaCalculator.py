#Joel Baanennul
#Pizza calculator
from ast import Try
prijs_pizza_large = 12
prijs_pizza_medium = 10
prijs_pizza_small = 8
aantal_large = "Geen goed getal"
aantal_medium = "Geen goed getal"
aantal_small = "Geen goed getal"
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
try:
    prijs_large = aantal_large * prijs_pizza_large
except:
    prijs_large = 0
try:
    prijs_medium = aantal_medium * prijs_pizza_medium
except:
    prijs_medium = 0
try:
    prijs_small = aantal_small * prijs_pizza_small
except:
    prijs_small = 0
totaal_prijs = prijs_large + prijs_medium + prijs_small

print("-----------------------------------------")
print("| Prijs : €", totaal_prijs)
if prijs_large > 0:    
    print("| Voor : ", aantal_small,"kleine pizzas;")
if prijs_medium > 0:    
    print("| Voor : ", aantal_medium,"medium pizzas;")
if prijs_small > 0:    
    print("| Voor : ", aantal_large,"large pizzas;")
print("-----------------------------------------")