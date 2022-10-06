geelkaas = input ("Is de kaas geel?\n")
if geelkaas == "ja":
    gatenkaas = input("Zitten er gaten er in?\n")
    if gatenkaas == "ja":
        duurkaas = input("Is de kaas belachelijk duur?\n")
        if duurkaas == "ja":
            print("Jou kaas is Emmenthaler")
        elif duurkaas == "nee":
            print("Jou kaas is Leerdammer")
    elif gatenkaas == "nee":
        hardkaas = input("Is de kaas hard als steen?\n")
        if hardkaas == "ja":
            print("Jou kaas is Parmigiano Reggiano")
        elif hardkaas == "nee":
            print("Jou kaas is Goudse Kaas")
elif geelkaas == "nee":
    blauwkaas = input("Heeft de kaas blauw schimmel?\n")
    if blauwkaas == "ja":
        korstkaas1 = input("Heeft de kaas een korst?\n")
        if korstkaas1 == "ja":
            print("Jou kaas is Blue de Rochbaron")
        elif korstkaas1 == "nee":
            print("Jou kaas is Foume d'Ambert")
    elif blauwkaas == "nee":
        korstkaas2 = input("Heeft de kaas een korst?\n")
        if korstkaas2 == "ja":
            print("Jou kaas is Camembert")
        elif korstkaas2 == "nee":
            print("Jou kaas is Mozzarella")
else:
    print("je hebt een foutje gemaakt")