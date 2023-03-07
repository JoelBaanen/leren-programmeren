import random
heelwarm = "je bent heel warm"
beetjewarm = "je bent warm"
ronde = 20
guesses = 10
score = 0
rondenleft = ronde
eindscore = 0
while 1 < ronde:
    getal = random.randint(0,1000)
    guesses = 10
    for b in range(guesses):
        geradengetal = int(input("Welke getal denk jij dat het is?"))
        print(getal)
        guesses -= 1
        if geradengetal == getal:
            ronde -= 1
            score += 10 - guesses 
            print("Your score is",score,"you have",ronde,"rounds left to go")
            eindscore += score
            if ronde == 0:
                print("Your final score is",eindscore)
            else:
                getal = random.randint(0,1000)
        elif geradengetal > getal:
            hogeroflaager = "te hoog"
            if getal + 20 > geradengetal:
                warm = heelwarm
            elif getal + 50 > geradengetal:
                warm = beetjewarm
            else:
                warm = "."
        elif geradengetal < getal:
            hogeroflaager = "te laag"
            if getal - 20 < geradengetal:
                warm = heelwarm
            elif getal - 50 < geradengetal:
                warm = beetjewarm
            else:
                warm = " "
        print("jij bent", hogeroflaager, warm)
        if guesses == 0:
            score += 10        