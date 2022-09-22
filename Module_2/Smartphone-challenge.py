prijs_samsung = int(input("Hoe duur is de samsung?\n"))
prijs_iphone = int(input("Hoe duur is de iphone?\n"))
if prijs_samsung > prijs_iphone:
    print("De samsung is het duurst, de kost:", prijs_samsung,"Euro")
    print("De iphone is het goedkoopst, de telefoon kost:", prijs_iphone,"Euro")
    if prijs_iphone > 900 and prijs_samsung > 900:
        print("Het advies is dus om geen telefoon te kopen, ze zijn te duur") 
    elif prijs_iphone > prijs_samsung:
        verschil = prijs_iphone - prijs_samsung
        if verschil > 50: 
            print("De advies is dus de samsung te kopen. Deze is namelijk", verschil, "euro goedkoper")
        elif verschil < 50:
            print("De advies is dus de iphone te kopen. Deze is namelijk", verschil, "euro duurder")
    elif prijs_iphone < prijs_samsung:
            verschil = prijs_samsung - prijs_iphone
            print("De advies is dus de iphone te kopen. Deze is namelijk", verschil, "euro goedkoper")  
elif prijs_iphone > prijs_samsung:
    print("De samsung is het goedkoopst, de kost:", prijs_samsung,"Euro")
    print("De iphone is het duurst, de telefoon kost:", prijs_iphone,"Euro")
    if prijs_iphone > 900 or prijs_samsung > 900:       
        print("Het advies is dus om geen telefoon te kopen, ze zijn te duur.")
    elif prijs_iphone > prijs_samsung:
        verschil = prijs_iphone - prijs_samsung
        if verschil > 50:  
            print("De advies is dus de samsung te kopen. Deze is namelijk", verschil, "euro goedkoper")
        elif verschil < 50:
            
            print("De advies is dus de iphone te kopen. Deze is namelijk", verschil, "euro duurder")
    elif prijs_iphone < prijs_samsung:
            verschil = prijs_samsung - prijs_iphone
            print("De advies is dus de iphone te kopen. Deze is namelijk", verschil, "euro goedkoper")
elif prijs_samsung == prijs_iphone:
    print("De samsung is even duur, de kost:", prijs_samsung,"Euro")
    print("De iphone is even duur, de telefoon kost:", prijs_iphone,"Euro")
    if prijs_iphone > 900 or prijs_samsung > 900:       
        print("Het advies is dus om geen telefoon te kopen, ze zijn te duur.")
    elif prijs_iphone > prijs_samsung:
        verschil = prijs_iphone - prijs_samsung
        if verschil > 50:  
            print("De advies is dus de samsung te kopen. Deze is namelijk", verschil, "euro goedkoper")
        elif verschil < 50:
            
            print("De advies is dus de iphone te kopen. Deze is namelijk", verschil, "euro duurder")
    elif prijs_iphone < prijs_samsung:
            verschil = prijs_samsung - prijs_iphone
            print("De advies is dus de iphone te kopen. Deze is namelijk", verschil, "euro goedkoper")