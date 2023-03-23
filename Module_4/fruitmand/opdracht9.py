from fruitmand import fruitmand

colours = []
for fruit in fruitmand:
    if fruit['name'] == 'druif':
        fruitmand.remove(fruit)
for x in fruitmand:
    if x['color'] not in colours:
        colours.append(x['color'])
print(", ".join(colours))