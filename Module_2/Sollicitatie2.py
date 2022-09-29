from re import A
print("----------------------------------")
print("-   Sollicitatie gesprek eisen   -")
print("----------------------------------")
print("- Dit is een programma die snel  -")
print("- checkt of jij aan alle eisen   -")
print("- voldoet en vraagt ook wat      -")
print("- vragen over jouw               -")
print("----------------------------------")
a = 1
naam = input("Wat is jouw naam?(voor)")
gender = input("Bent u een man of een vrouw?m/v\n")
if gender == "m":
    snor = input("Heeft uw een snor?j/n\n")
    if snor == "j":
        a += 1
        snor_lengte = int(input("Hoe lang is uw snor?(cm)\n"))
        if snor_lengte > 10:
            a += 1
        else: 
            a += -1
    else:
        a += -1
if gender == "v":
    haar_kleur = input("Welke kleur is uw haar?\n")
    if haar_kleur == "rood":
        a += 1
    else:
        a += 1
    gekrulled = input("Is uw haar gekrulled?j/n\n")
    if gekrulled == "j":
        a += 1
    else:
        a += -1
    haar_lengte = int(input ("Hoe lang is uw haar?(cm)\n"))
    if haar_lengte > 20:
        a += 1
    else:
        a += -1
mbo = input("Heb jij een MBO-4 diploma voor ondernemen?j/n\n")
if mbo == "j":
    a += 1
else:
    a += -1
rijbewijs = input("Heb jij een vrachtwagen rijbewijs?j/n\n")
ervaring_vraag = input("Heb jij praktijd ervaring in acrobatiek of ervaring met jongleren of praktijkervaring met dieren-dressuur?j/n\n")
if ervaring_vraag == "j":
    a += 1
    ervaring_welke = input("Welke heb jij(acrobatiek/jongleren/dieren-dressuur?\n")
    if ervaring_welke == "acrobatiek":
        acrobatiek_jaar = int(input("Hoeveel jaar heb jij ervaring?\n"))
        if acrobatiek_jaar > 3:
            a += 1                
        else:
                a += -1
    elif ervaring_welke == "jongleren":
        jongleren_jaar = int(input("Hoeveel jaar heb jij ervaring?\n"))
        if jongleren_jaar > 5:
            a += 1     
        else:
            a += -1                        
    elif ervaring_welke == "dieren-dressuur":                        
        dieren_jaar = int(input("Hoeveel jaar heb jij ervaring\n"))                        
        if dieren_jaar > 4:
            a += 1
        else:
            a += -1                                                                    
elif ervaring_vraag == "n":
    a += -1                            
else:                           
    print("Jij hebt iets fouts ingetyped")    
hoed = input("Ben jij in bezit van een hoge hoed?j/n\n")
if hoed == "j":
    a += 1                     
else:
    a += -1    
gewicht = int(input("Hoeveel weeg je?(kg)\n"))
if 120 > gewicht > 90:
    a += 1
else:
    a += -1
lengte = int(input("Hoe lang ben jij?(cm)\n"))
if 220 > lengte > 150:
    a += 1
else:
    a += -1
print(a)
if a == 9 or a == 10:
    print("Beste", naam)
    print ("Jij voldoet aan alles eisen jij mag een sollicitatie gesprek opvragen.")
else:
    print("Beste", naam)  
    print("Jij voldoet niet aan al onze eisen jij zou niet toegestaan worden. ")