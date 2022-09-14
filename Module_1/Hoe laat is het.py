print("Hoe laat is het?")
uur = int(input("Uur"))
min = int(input("Minuten"))

totale = uur * 60
totaal = totale + min
max_min_totaal = 1440 - totaal
antwoord_min = 60 - min
nw = max_min_totaal - antwoord_min
nu = nw / 60


print("Jij hebt nog",nu,"uur en", antwoord_min,"minuten in het dag.")