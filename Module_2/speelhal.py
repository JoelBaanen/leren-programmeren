# 7.45 euro per dag per persoon
#vip vr room is 37 cent per 5 min
entree = float(745)
vip = float(37/5)

personen = float(input("Met hoeveel mensen zijn jullie?\n"))
tijd_vip = float(input("Hoe langen blijven jullie in de vip vr room?\n"))

totaal_entree = entree * personen
totaal_vip = tijd_vip * personen * vip

totaal = (totaal_entree + totaal_vip) / 100

print("Dit geweldige dagje-uit met", personen, "mensen in de Speelhal met", tijd_vip, "minuten VR kost je maar",totaal, "euro.")