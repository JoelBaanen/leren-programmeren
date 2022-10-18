gastheer = input('Wie is de gastheer?')
gasten = True
drank = True
chips = True
if drank and (gasten or gastheer == True):
    print('Start the Party')
else:
    print('No Party')