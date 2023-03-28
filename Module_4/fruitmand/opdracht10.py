from fruitmand import fruitmand

sortedfruitmand = sorted(fruitmand, key=lambda d: d['weight'], reverse=True)
for x in sortedfruitmand:
    print(x['name'])
    print(x['weight'])