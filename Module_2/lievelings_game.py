#lievelings game
import random
game=input("Wat is jouw lievelings game?")
TrueOrFalse = bool(random.randint(0,1))
if TrueOrFalse:
    print('Die game is best wel goed.')
else:
    print('TBH,',game,' is best wel trash...')