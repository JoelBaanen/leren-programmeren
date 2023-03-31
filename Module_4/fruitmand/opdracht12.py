from fruitmand import fruitmand
translated = ""
length = []
lengthlong = []
def translation(fruitColor: str) -> str:
    translated = {"yellow": "gele", "green": "groene", "orange": "oranje", "red": "rode", "brown": "bruine", "pink": "roze", "purple": "paarse", "black": "zwarte"}
    if fruitColor in translated:
        return translated[fruitColor]
    else:
        return fruitColor
    
for x in fruitmand:
    lengthlong.append(len(x['name']))

index = lengthlong.index(max(lengthlong))
longestFruit = fruitmand[index]

print(f"De {longestFruit['name']} ({len(longestFruit['name'])} letters) heeft een {translation(longestFruit['color'])} kleur en een gewicht van {longestFruit['weight'] / 1000}KG")