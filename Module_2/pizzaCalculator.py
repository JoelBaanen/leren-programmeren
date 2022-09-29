#Joel Baanen
#Pizza calculator

vraag_small = int(input("Hoeveel kleine pizzas wilt u (€7.99)?\n"))
vraag_medium = int(input("Hoeveel medium pizzas wilt u (€9.99)?\n"))
vraag_large = int(input("Hoeveel grote pizzas wilt u (€12.99)?\n"))

prijs_small = vraag_small * 7.99
prijs_medium = vraag_medium * 9.99
prijs_large = vraag_large * 12.99

totaal_prijs = prijs_large + prijs_medium + prijs_small
totaal_prijs = round(totaal_prijs, 2)

print("-----------------------------------------")
print("| Prijs : €", totaal_prijs)
print("| Voor : ", vraag_small,"kleine pizzas;", vraag_medium,"medium pizzas;", vraag_large,"large pizzas;")
print("-----------------------------------------")