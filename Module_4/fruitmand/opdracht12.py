from fruitmand import fruitmand
translated = ""
length = []
lengthnr = []
def translation(fruitColor: str) -> str:
    translated = {"yellow": "gele", "green": "groene", "orange": "oranje", "red": "rode", "brown": "bruine", "pink": "roze", "purple": "paarse", "black": "zwarte"}
    if fruitColor in translated:
        return translated[fruitColor]
    else:
        return fruitColor
    
    