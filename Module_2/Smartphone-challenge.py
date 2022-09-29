from cProfile import run


prijs_samsung = int(input("Hoe duur is de samsung?\n"))
prijs_iphone = int(input("Hoe duur is de iphone?\n"))
prijs_asus = int(input("Hoe duur is de zenfone?\n"))
if 1 + 1 == 2:
    if (prijs_samsung < 900) > (prijs_iphone < 900) > (prijs_asus < 900):
        prijs_duur = prijs_samsung
        prijs_tussen = prijs_iphone
        prijs_goedkoop = prijs_asus
        goedkoop = "asus"
        tussen = "iphone"
        duur = "samsung"
        verschil = prijs_iphone - prijs_goedkoop
    elif (prijs_asus < 900) > (prijs_iphone < 900) > (prijs_samsung< 900) :
        prijs_duur = prijs_asus
        prijs_tussen = prijs_iphone
        prijs_goedkoop = prijs_samsung
        goedkoop = "samsung"
        tussen = "iphone"
        duur = "asus"
        verschil = prijs_iphone - prijs_goedkoop
    elif (prijs_samsung < 900) > (prijs_asus < 900) >  (prijs_iphone < 900):
        prijs_duur = prijs_samsung
        prijs_tussen = prijs_asus
        prijs_goedkoop = prijs_iphone
        goedkoop = "iphone"
        duur = "samsung"
        tussen = "asus"
        verschil = prijs_iphone - prijs_goedkoop
    elif (prijs_asus < 900) > (prijs_samsung < 900) > (prijs_iphone < 900):
        prijs_duur = prijs_asus
        prijs_tussen = prijs_samsung
        prijs_goedkoop = prijs_iphone
        tussen = "samsung"
        duur = "asus"
        goedkoop = "iphone"
        verschil = prijs_iphone - prijs_goedkoop
    elif (prijs_iphone < 900) > (prijs_asus < 900) > (prijs_samsung < 900):
        prijs_duur = prijs_iphone
        prijs_tussen = prijs_asus
        prijs_goedkoop = prijs_samsung
        duur = "iphone"
        goedkoop = "samsung"
        tussen = "asus"
        verschil = prijs_iphone - prijs_goedkoop
    elif (prijs_iphone < 900) > (prijs_samsung < 900) > (prijs_asus < 900):
        prijs_duur = prijs_iphone
        prijs_tussen = prijs_samsung
        prijs_goedkoop = prijs_asus
        duur = "iphone"
        goedkoop = "asus"
        tussen = "samsung"
        verschil = prijs_iphone - prijs_goedkoop
    else:
        print("Het advies is dus geen telefoon te kope, ze zijn te duur")
if 50 < verschil:
    prijs_keuze = prijs_iphone
    keuze = "iphone"
    verschil_keuze_i1 = prijs_iphone - prijs_goedkoop
    verschil_keuze_i2 = prijs_duur - prijs_iphone
    print("Het advies is de iphone te kopen. Deze is namelijk", verschil_keuze_i1,"duurder da de",goedkoop,"en",verschil_keuze_i2,"goedkoper dan de", duur)
else:
    prijs_keuze = prijs_goedkoop
    keuze = goedkoop 
    verschil_keuze = prijs_tussen - prijs_goedkoop
    verschil_keuze_2 = prijs_duur - prijs_goedkoop
    print("Het advies is dus",keuze,"te kopen. Deze is namelijk", prijs_keuze,"euro goedkoper dan de",keuze,"en",keuze,"euro goedkoper dan de",)       
print("De ", duur," is het duurst, de kost:", prijs_duur,"Euro")
print("De ", goedkoop," is het goedkoopst, de telefoon kost:", prijs_goedkoop,"Euro")
print("De", tussen,"zit er tussen in met:",prijs_tussen,"Euro")