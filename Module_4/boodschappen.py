lijst = {}
loop = True

while loop == True:
    product = input("Wat voor product wilt uw toevoegen?")
    aantal = int(input("Hoeveel wil jij dervan?"))

    if product == lijst:
        lijst[product] += aantal
    else:
        lijst.update({product:aantal})
    quit = input("typ Stop als je wilt stoppen.")
    if quit == "stop":
        loop = False
print("----------------------------")
print('')
print(lijst)
print('')
print("-----------------------------")