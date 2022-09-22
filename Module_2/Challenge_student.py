getal = float(input("Voer een getal in?\n"))


if getal >= 10.0:
    print("Je bent een geweldige student")
elif getal > 7.9 and getal < 10.0:
    print("Je bent een goede student!")
elif getal > 5.9 and getal < 8.0:
    print("Je bent een gemiddelde student")
elif getal > 3.9 and getal < 6.0:
    print("Waarschuwing!")
elif getal > 1.0 and getal < 4.0:
    print("Brief naar de ouders")

