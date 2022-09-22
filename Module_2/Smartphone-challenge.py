prijs_samsung = int(input("Hoe duur is de samsung?\n"))
prijs_iphone = int(input("Hoe duur is de iphone?\n"))
prijs_asus = int(input("Hoe duur is de zenfone?\n"))
if prijs_samsung > prijs_iphone > prijs_asus:
    prijs_duur = prijs_samsung
    prijs_tussen = prijs_iphone
    prijs_goedkoop = prijs_asus
    goedkoop = "asus"
elif prijs_asus > prijs_iphone > prijs_samsung:
    prijs_duur = prijs_asus
    prijs_tussen = prijs_iphone
    prijs_goedkoop = prijs_samsung
elif prijs_samsung > prijs_asus >  prijs_iphone:
    prijs_duur = prijs_samsung
    prijs_tussen = prijs_asus
    prijs_goedkoop = prijs_iphone
elif prijs_asus > prijs_samsung > prijs_iphone:
    prijs_duur = prijs_asus
    prijs_tussen = prijs_samsung
    prijs_goedkoop = prijs_iphone
    tussen = "samsung"
elif prijs_iphone > prijs_asus > prijs_samsung:
    prijs_duur = prijs_iphone
    prijs_tussen = prijs_asus
    prijs_goedkoop = prijs_samsung
elif prijs_iphone > prijs_samsung > prijs_asus:
    prijs_duur = prijs_iphone
    prijs_tussen = prijs_samsung
    prijs_goedkoop = prijs_asus
    duur = "iphone"
    goedkoop = "asus"
    tussen = "samsung"

print("De ", ," is het duurst, de kost:", prijs_duur,"Euro")
print("De ", ," is het goedkoopst, de telefoon kost:", prijs_goedkoop,"Euro")
print("De", ,"zit er tussen in met:",prijs_tussen,"Euro")




if prijs_iphone > 900 and prijs_samsung > 900:
    print("Het advies is dus om geen telefoon te kopen, ze zijn te duur") 
if prijs_iphone > prijs_samsung:
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
