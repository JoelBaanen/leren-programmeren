# 17 croissantjes 39cent per
# 2 stokbroden 2,78 euro per
# 3 kortsing bonnen 50 per

croissant = float(0.39)
stokbroden = float(2.78)
korting = float(0.50)

aantal1 = float(input("Hoeveel croissantjes wilt uw?\n"))
aantal2 = float(input("Hoeveel stokbroden wilt uw?\n"))
aantal3 = float(input("Hoeveel kortings bonnen heb je?\n"))

totale1 = croissant * aantal1
totale2 = stokbroden * aantal2
totale3 = korting * aantal3
Totaal_alles = totale1 + totale2 - totale3

print("De feestlunch kost je bij de bakker", Totaal_alles, "euro voor de", int(aantal1), "croissantjes en de", int(aantal2),"stokbroden als de", int(aantal3),"kortingsbonnen nog geldig zijn.")

