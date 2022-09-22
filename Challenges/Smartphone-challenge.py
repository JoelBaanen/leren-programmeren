prijs_samsung = int(input("Hoe duur is de samsung?\n"))
prijs_iphone = int(input("Hoe duur is de iphone?\n"))
if prijs_iphone > prijs_samsung:
    verschil = prijs_iphone - prijs_samsung
    if verschil > 50:
        print("De iphone is het duurst, de kost:", prijs_iphone,"Euro")
        print("De samsung is het goedkoopst, de telefoon kost:", prijs_samsung,"Euro")
        print("De advies is dus de samsung te kopen. Deze is namelijk", verschil, "euro goedkoper")
    elif verschil < 50:
        print("De iphone is het duurst, de kost:", prijs_iphone,"Euro")
        print("De samsung is het goedkoopst, de telefoon kost:", prijs_samsung,"Euro")
        print("De advies is dus de iphone te kopen. Deze is namelijk", verschil, "euro duurder")
elif prijs_iphone < prijs_samsung:
    verschil = prijs_samsung - prijs_iphone
    print("De iphone is het duurst, de kost:", prijs_iphone,"Euro")
    print("De samsung is het goedkoopst, de telefoon kost:", prijs_samsung,"Euro")
    print("De advies is dus de iphone te kopen. Deze is namelijk", verschil, "euro goedkoper")
