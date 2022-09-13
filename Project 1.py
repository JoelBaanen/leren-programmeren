import math



#Aantallen
bloem = 800/20  #bloem
melk = 500/20  #melk
eien = 3/20    #eien
boter = 30/20   #boter
zout = 1/20    #zout


aantal = float(input('Hoeveel Pannekoeken wilt u?\n'))

bloem = aantal * bloem
melk = aantal * melk
eien = aantal * eien
boter = aantal * boter
zout = aantal * zout


print("Voor", aantal, "Pannekoeken")
print("Bloem", math.ceil(bloem))
print("Melk", math.ceil(melk))
print("Eien", math.ceil(eien)) 
print("Boter", math.ceil(boter))
print("Zout", math.ceil(zout))
print("**" )
print("eetsmakkelijk")

