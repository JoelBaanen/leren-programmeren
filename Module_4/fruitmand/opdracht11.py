from fruitmand import fruitmand
from fruitmand import fruitmand

loop = False
round = 0
nietrond = 0

while not loop:
    keuzekleur = input("Geef een kleur op: ").lower()
    for x in fruitmand:
        if keuzekleur == x['colour']:
            if x['round']:
                round += 1
            else:
                nietrond += 1
            loop = True
    if not loop:
        print(f"De kleur {keuzekleur} zit er niet in de fruitmand")

if round > nietrond:
    print(f'Er zijn {round - nietrond} meer ronde vruchten dan niet ronde vruchten in de kleur {keuzekleur}')
elif round < nietrond:
        print(f'Er is {abs(round - nietrond)} minder ronde vruchten dan niet ronde vruchten in de kleur {keuzekleur}')
else:
    print(f'Er zijn {round} ronde vruchten en {nietrond} niet ronde vruchten in de kleur {keuzekleur}')
