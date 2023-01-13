welke_groep = input("Welke groep is dit?")
lijn = "--"
puntenland1 = 0
puntenland2 = 0
puntenland3 = 0

land1 = input("Welke land is land 1?")
land2 = input("Welke land is land 2?")
land3 = input("Welke land is land 3?")
#Wedstrijd 1
wedstrijd1_land1 = int(input("In wedstrijd 1 hoeveel doelpunten scored land 1?"))
wedstrijd1_land2 = int(input("In wedstrijd 1 hoeveel doelpunten scored land 2?"))
if wedstrijd1_land1 > wedstrijd1_land2:
    puntenland1 += 3
    winnaar1 = land1
elif wedstrijd1_land2 > wedstrijd1_land1:
    puntenland2 += 3
    winnaar1 = land2

print("De winnaar van wedstrijd 1 was",winnaar1)
print(land1,"Heeft",puntenland1,"punten")
print(land2,"Heeft",puntenland2,"punten")
print(land3,"Heeft",puntenland3,"punten")
#Wedstrijd 2
wedstrijd2_land2 = int(input("In wedstrijd 2 hoeveel doelpunten scored land 2?"))
wedstrijd2_land3 = int(input("In wedstrijd 2 hoeveel doelpunten scored land 3?"))
if wedstrijd2_land2 > wedstrijd2_land3:
    puntenland2 += 3
    winnaar2 = land2
elif wedstrijd2_land3 > wedstrijd2_land2:
    puntenland3 += 3
    winnaar2 = land3
print("De winnaar van wedstrijd 2 was",winnaar2)
print(land1,"Heeft",puntenland1,"punten")
print(land2,"Heeft",puntenland2,"punten")
print(land3,"Heeft",puntenland3,"punten")
#Wedstrijd 3
wedstrijd3_land1 = int(input("In wedstrijd 3 hoeveel doelpunten scored land 1?"))
wedstrijd3_land3 = int(input("In wedstrijd 3 hoeveel doelpunten scored land 3?"))
if wedstrijd3_land1 > wedstrijd3_land3:
    puntenland1 += 3
    winnaar3 = land1
elif wedstrijd3_land3 > wedstrijd3_land1:
    puntenland3 += 3
    winnaar3 = land3

print("Wedstrijd -- thuis -- uit -- Doelpunten thuis - Doelpunten uit -- Winnaar")
print("   1   ",lijn,land1,lijn,land2,lijn,wedstrijd1_land1,lijn,wedstrijd1_land2,winnaar1)
print("   3   ",lijn,land2,lijn,land3,lijn,wedstrijd2_land2,lijn,wedstrijd2_land3,winnaar2)
print("   3   ",lijn,land3,lijn,land1,lijn,wedstrijd3_land3,lijn,wedstrijd3_land1,winnaar3)
print("----------------------------------------------------------")
#Vraag 2
land1_totaal_doelen = wedstrijd1_land1 + wedstrijd3_land1
land2_totaal_doelen = wedstrijd1_land2 + wedstrijd1_land2
land3_totaal_doelen = wedstrijd3_land3 + wedstrijd2_land3

land1_totaal_tegen_doel = wedstrijd1_land2 + wedstrijd3_land3
land2_totaal_tegen_doel = wedstrijd2_land3 + wedstrijd1_land1
land3_totaal_tegen_doel = wedstrijd3_land1 + wedstrijd2_land2

#Vraag 3
print("----------------------------------")
print("Overzicht groep",welke_groep)
print("land -- Doelsaldo -- Puntentotaal")
print(land1,lijn,land1_totaal_doelen,";",land1_totaal_tegen_doel)
print(land2,lijn,land2_totaal_doelen,";",land2_totaal_tegen_doel)
print(land3,lijn,land3_totaal_doelen,";",land3_totaal_tegen_doel)
print("----------------------------------")

#Vraag 4
#zit boven

#Vraag 5

print("De winnaar van wedstrijd 3 was",winnaar3)
print(land1,"Heeft",puntenland1,"punten")
print(land2,"Heeft",puntenland2,"punten")
print(land3,"Heeft",puntenland3,"punten")