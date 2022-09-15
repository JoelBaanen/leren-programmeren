# 17 croissantjes 39cent per
# 2 stokbroden 2,78 euro per
# 3 kortsing bonnen 50 per
 
croissant = 0.39
stokbroden = 2.78
korting = 0.50

aantal_croissant = int(input("Hoeveel croissantjes wilt je?\n"))
aantal_stokbroden = int(input("Hoeveel stokbroden wilt je?\n"))
aantal_korting = int(input("Hoeveel kortings bonnen heb je?\n"))

totale_croissant = croissant * aantal_croissant
totale_stokbroden = stokbroden * aantal_stokbroden
totale_korting = korting * aantal_korting

Totaal_alles = totale_croissant + totale_stokbroden - totale_korting
Totaal_alles = round(Totaal_alles, 2)

print("De feestlunch kost je bij de bakker", Totaal_alles, "euro voor de", int(aantal_croissant), "croissantjes en de", int(aantal_stokbroden),"stokbroden als de", int(aantal_korting),"kortingsbonnen nog geldig zijn.")

