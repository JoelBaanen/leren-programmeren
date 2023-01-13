#Elden Ring
import random
fout_melding = "Jij heb waarschijnlijk iets niet goeds getypt"
karakter_naam = input("Name your character.")
intro_text = """to the world of Elden Ring. Where your worst fears become reality"""
tutorial_text = """Jij begint met niks. Jij moet betere wapens vinden om sterk 
genoeg te worden om dus de volgende vijand te verslaan anders 
is het heel erg lastig en heb jij heel veel geluk nodig.
Je begint ook met 2 moves die je doet 
Move 1 doet de helft zoveel damage dan move 2 maar raakt altijd. Er wordt
ook later verteld als jij een nieuwe move krijgt wat ie doet etc.
Move 2 is een high risk high reward move want jij hebt een kans 
om zojuist te missen maar ook een kans om meer damage te doen tegen jou vijand. """
dmg_text = "You hit for"
miss = "You missed your attack"
print("Welcome", karakter_naam, intro_text)
print(tutorial_text)
vijand_hp = 20
karakter_hp = 100
karakter_dmg = 5
move_2dmg = karakter_dmg * 2
win_msg = "You have defeated the enemy"
soldaat_tekst = """Jij wordt wakker in de midden van een grote hal met 
een zittende soldaat aan het einde voor een deur."""
print(soldaat_tekst)
soldaat_relatie = int(input ("Wat doe jij met het soldaat? 1 - Probeer jij langs te gaan of 2 - probeer jij met hem te praten?"))
if soldaat_relatie == 1:
    print("Hij wilt niet dat jij langs gaat zomaar dus hij begint een duel met jou.")
    while True:
        if vijand_hp > 1:
            move_keuze = int(input("Welke move wil jij doen op de soldaat? 1 of 2"))
            if move_keuze == 1:
                vijand_hp = vijand_hp - karakter_dmg
                print(dmg_text ,karakter_dmg,"they have",vijand_hp,"hp left")
                continue
            elif move_keuze == 2:
                move_hit = bool(random.randint(0,1))
                if move_hit:
                    vijand_hp = vijand_hp - (karakter_dmg * 2)
                    print(dmg_text, move_2dmg,"they have",vijand_hp,"hp left")
                    continue
                else:
                    print(miss)
                    continue
            else:
                print(fout_melding)
        else:
            print(win_msg)
            karakter_dmg = karakter_dmg + 5
            next_stage = True
            break
elif soldaat_relatie == 2:
    print("Jullie hebben een gesprek en hij laat jou langs.")
    next_stage = True
else:
    print(fout_melding)
if next_stage == True:
    next_stage = False
    print("Jij volgt een pad tot jij aan het ingang van een kasteel terecht komt.")
    kasteel_ingang_keuze = int(input("Hoe ga jij in het kasteel? 1 - main ingang of 2 - side ingang?"))
    if kasteel_ingang_keuze == 1:
        vijand_hp = 30
        vijand_dmg = 15
        print("Jij komt een groep van 3 kleine soldaten tegen en zij gaan je vechten.")
while True:
    move_keuze = int(input("Welke move ga jij doen?1/2"))
    if move_keuze == 1:
        vijand_hp = vijand_hp - karakter_dmg
        if 0 >= vijand_hp:
            print("Jij hebt ze verslaan.")
            next_stage = True
            break
        elif 10 >= vijand_hp:
             print("Er is nog een soldaat over.")
             vijand_dmg = 5
        elif 20 >= vijand_hp:
            print("Jij hebt een soldaat verslaan.")
            vijand_dmg = 10
        else:
            print(fout_melding)
    elif move_keuze == 2:
        move_hit = bool(random.randint(0,1))
        if move_hit == 1:
            vijand_hp = vijand_hp - (karakter_dmg * 2)
                
            if 0 >= vijand_hp:
                print("Jij hebt ze verslaan.")
                next_stage = True
                karakter_hp = 200
                karakter_dmg = 20
                break
            elif 10 >= vijand_hp:
                print("Er is nog een soldaat over.")
                vijand_dmg = 5
            elif 20 >= vijand_hp:
                print("Jij hebt een soldaat verslaan.")
                vijand_dmg = 10
            else:
                print(fout_melding)
        elif  move_hit == 0:
            print(miss)
    else:
        print(fout_melding)
    if 0 > karakter_hp:
        print("You died you must start again.")
    karakter_hp = karakter_hp - vijand_dmg
    print("jij wordt gehit voor", vijand_dmg,"Jij hebt",karakter_hp,"hp nog over")
if kasteel_ingang_keuze == 2:
    next_stage = False
    kist_keuze = input("Jij vindt een kist in het kasteel. Wat doe jij dermee? open/negeer")
    if kist_keuze == "open":
        karakter_hp = 400
        print("jij vindt een set van sterke armor.")
        next_stage = True
    elif kist_keuze == "negeer":
        next_stage = True
if next_stage == True:
    print("Jij bevindt jezelf voor de koning van het kasteel die jij nu moet vechten.")
    boss_vijand_hp = 200
while True:
    move_keuze = int(input("Welke move ga jij doen? 1/2"))
    if move_keuze == 1:
        boss_vijand_hp = boss_vijand_hp - karakter_dmg
        dmg_gedaan = karakter_dmg
        print("Jij dee", dmg_gedaan, "dmg en hij heeft nog", boss_vijand_hp,"hp over.")
        if 0 >= boss_vijand_hp:
            print("Jij hebt de boss verslaan en hebt de game gekompleet.")
            break
    elif move_keuze == 2:
        boss_vijand_hp = boss_vijand_hp - (karakter_dmg * 2)
        dmg_gedaan = (karakter_dmg * 2)
        print("Jij dee", dmg_gedaan, "dmg en hij heeft nog", boss_vijand_hp,"hp over.")
        if 0 >= boss_vijand_hp:
            print("Jij hebt de boss verslaan en hebt de game gekompleet.")
            break
    karakter_hp = karakter_hp - 30
    print("Jij wordt gehit voor 30 jij hebt nog", karakter_hp, "hp")
    if 0 > karakter_hp:
        print("You died you must start again.")
        break