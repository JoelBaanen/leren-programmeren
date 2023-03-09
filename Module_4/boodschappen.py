lijst = {}
loop = True

while loop == True:
    product = input("Wat voor product wilt uw toevoegen?")
    aantal = int(input("Hoeveel wil jij dervan?"))

    if product == lijst:
        lijst[product] += aantal
    else:
        lijst.update({lijst[product]})