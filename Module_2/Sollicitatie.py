print("----------------------------------")
print("-   Sollicitatie gesprek eisen   -")
print("----------------------------------")
print("- Dit is een programma die snel  -")
print("- checkt of jij aan alle eisen   -")
print("- voldoet en vraagt ook wat      -")
print("- vragen over jouw               -")
print("----------------------------------")
snorlengte = ""
haarlengte = ""
naam = input("Wat is jouw naam?(voor)")
if naam == "Joel":
    print("Hoe gaat alles vandaag?")
gender = input("Bent u een man of een vrouw?m/v\n")
if gender == "m":
    snor = input("Heeft uw een snor?j/n")
    if snor == "j":
        snor_lengte = int(input("Hoe lang is uw snor?(cm)"))
    if snor == "n":
        whysnor = input("Why?")
elif gender == "v":
    haar_kleur = input("Welke kleur is uw haar?")
    if haar_kleur == "rood":
        gekrulled = input("Is uw haar gekrulled?j/n")
        if gekrulled == "j":
            haar_lengte = int(input ("Hoe lang is uw haar?(cm)"))
    if haar_kleur == "blauw":
        print("Ben je emo?")
mbo = input("Heb jij een MBO-4 diploma voor ondernemen?j/n")
rijbewijs = input("Heb jij een vrachtwagen rijbewijs?j/n")
jongleren = int(input("Hoeveel jaar jongleert u?"))
dieren_dressuur = int(input("Hoeveel jaar dresseert u dieren?"))
acrobatiek = int(input("Hoeveel jaar doet u acrobatiek?\n"))   
hoed = input("Ben jij in bezit van een hoge hoed?j/n")
gewicht = int(input("Hoeveel weeg je?(kg)"))
lengte = int(input("Hoe lang ben jij?(cm)"))
if (snor_lengte >= 10 or haar_lengte >= 20) and mbo == "j" and rijbewijs == "j" and (jongleren >= 5 or dieren_dressuur >= 4 or acrobatiek >= 3) and hoed == "j" and (90 < gewicht < 120) and (150 < lengte < 220):
    print ("Beste", naam, "Jij voldoet aan alles eisen jij mag een sollicitatie gesprek opvragen.")
else:  
    print("Beste", naam, "Jij voldoet niet aan al onze eisen jij zou niet toegestaan worden. ")