

gender = input("Bent u een man of een vrouw?\n")
mbo = input("Heb jij een MBO-4 diploma voor ondernemen?j/n\n")
if mbo == "j":
    rijbewijs = input("Heb jij een vrachtwagen rijbewijs?j/n\n")
    if rijbewijs ==  "j":
        if gender == "man":
            snor = input("Heeft uw een snor?\n")
            if snor == "j":
                snor_lengte = int(input("Hoe lang is uw snor?(cm)\n"))
                if snor_lengte > 10:
                    gewicht = int(input("Hoeveel weeg je?(kg)\n"))
                    if 120 > gewicht > 90:
                        lengte = int(input("Hoe lang ben jij?(cm)\n"))
                        if 220 > lengte > 150:
                            ervaring_vraag = input("Heb jij praktijd ervaring in acrobatiek of ervaring met jongleren of praktijkervaring met dieren-dressuur?j/n\n")
                            if ervaring_vraag == "j":
                                ervaring_welke = input("Welke heb jij(acrobatiek/jongleren/dieren-dressuur?\n")
                                if ervaring_welke == "acrobatiek":
                                    acrobatiek_jaar = int(input("Hoeveel jaar heb jij ervaring?\n"))
                                    if acrobatiek_jaar > 3:
                                        hoed = input("Ben jij in bezit van een hoge hoed?j/n\n")
                                        if hoed == "j":
                                            print("Jij voldoet aan alle eisen jij mag een solicitatie gesprek aanvragen.")
                                        else:
                                            print("Jij heb of iets fouts getyped of jij bent niet toegestaan voor een sollicitatie gesprek")
                                    else:
                                        print("Jij heb of iets fouts getyped of jij bent niet toegestaan voor een sollicitatie gesprek")
                                elif ervaring_welke == "jongleren":
                                    jongleren_jaar = int(input("Hoeveel jaar heb jij ervaring?\n"))
                                    if jongleren_jaar > 5:
                                        hoed = input("Ben jij in bezit van een hoge hoed?j/n\n")
                                        if hoed == "j":
                                            print("Jij voldoet aan alle eisen jij mag een solicitatie gesprek aanvragen.")
                                        else:
                                            print("Jij heb of iets fouts getyped of jij bent niet toegestaan voor een sollicitatie gesprek")
                                    else:
                                        print("Jij heb of iets fouts getyped of jij bent niet toegestaan voor een sollicitatie gesprek")
                                elif ervaring_welke == "dieren-dressuur":
                                    dieren_jaar = int(input("Hoeveel jaar heb jij ervaring\n"))
                                    if dieren_jaar > 4:
                                        hoed = input("Ben jij in bezit van een hoge hoed?\n")
                                        if hoed == "ja":
                                            print("Jij voldoet aan alle eisen jij mag een solicitatie gesprek aanvragen.")
                                        else:
                                            print("Jij heb of iets fouts getyped of jij bent niet toegestaan voor een sollicitatie gesprek")
                                    else:
                                        print("Jij heb of iets fouts getyped of jij bent niet toegestaan voor een sollicitatie gesprek")
                                else:
                                    print("Jij hebt iets fouts ingetypt")
                            elif ervaring_vraag == "nee":
                                    print("Jij ben niet toegestaan voor een sollicitatie gesprek")
                            else:
                                    print("Jij hebt iets fouts ingetyped")
                        else:
                            print("Jij ben niet toegestaan voor een sollicitatie gesprek")
                    else: 
                        print("Je ben niet toegestaan voor een sollicitatie gesprek")
            elif snor == "nee":
                print("Jij ben niet toegestaan voor een sollicitatie gesprek")
            else:
                print("Jij heb iets fout getyped")
        elif gender == "vrouw":
            haar_kleur = input("Welke kleur is uw haar?\n")
            if haar_kleur == "rood":
                haar_lengte = int(input ("Hoe lang is uw haar?(cm)\n"))
                if haar_lengte > 20:
                    gewicht = int(input("Hoeveel weeg je?(kg)\n"))
                    if 120 > gewicht > 90:
                        lengte = int(input("Hoe lang ben jij?(cm)\n"))
                        if 220 > lengte > 150:
                            ervaring_vraag = input("Heb jij praktijd ervaring in acrobatiek of ervaring met jongleren of praktijkervaring met dieren-dressuur?\n")
                            if ervaring_vraag == "ja":
                                ervaring_welke = input("Welke heb jij(acrobatiek/jongleren/dieren-dressuur?\n")
                                if ervaring_welke == "acrobatiek":
                                    acrobatiek_jaar = int(input("Hoeveel jaar heb jij ervaring?\n"))
                                    if acrobatiek_jaar > 3:
                                        hoed = input("Ben jij in bezit van een hoge hoed?\n")
                                        if hoed == "ja":
                                            print("Jij voldoet aan alle eisen jij mag een solicitatie gesprek aanvragen.")
                                        else:
                                            print("Jij heb of iets fouts getyped of jij bent niet toegestaan voor een sollicitatie gesprek")
                                    else:
                                        print("Jij heb of iets fouts getyped of jij bent niet toegestaan voor een sollicitatie gesprek")
                                elif ervaring_welke == "jongleren":
                                    jongleren_jaar = int(input("Hoeveel jaar heb jij ervaring?\n"))
                                    if jongleren_jaar > 5:
                                        hoed = input("Ben jij in bezit van een hoge hoed?\n")
                                        if hoed == "ja":
                                            print("Jij voldoet aan alle eisen jij mag een solicitatie gesprek aanvragen.")
                                        else:
                                            print("Jij heb of iets fouts getyped of jij bent niet toegestaan voor een sollicitatie gesprek")
                                    else:
                                        print("Jij heb of iets fouts getyped of jij bent niet toegestaan voor een sollicitatie gesprek")
                                elif ervaring_welke == "dieren-dressuur":
                                    dieren_jaar = int(input("Hoeveel jaar heb jij ervaring\n"))
                                    if dieren_jaar > 4:
                                        hoed = input("Ben jij in bezit van een hoge hoed?\n")
                                        if hoed == "ja":
                                            print("Jij voldoet aan alle eisen jij mag een solicitatie gesprek aanvragen.")
                                        else:
                                            print("Jij heb of iets fouts getyped of jij bent niet toegestaan voor een sollicitatie gesprek")
                                    else:
                                        print("Jij heb of iets fouts getyped of jij bent niet toegestaan voor een sollicitatie gesprek")
                                else:
                                    print("Jij hebt iets fouts ingetypt")
                            elif ervaring_vraag == "nee":
                                print("Jij ben niet toegestaan voor een sollicitatie gesprek")
                            else:
                                print("Jij hebt iets fouts ingetyped")
                        else:
                            print("Jij ben niet toegestaan voor een sollicitatie gesprek")
                    else: 
                            print("Je ben niet toegestaan voor een sollicitatie gesprek")
                else:
                    print("Jij heb of iets fouts getyped of jij bent niet toegestaan voor een sollicitatie gesprek")
        else:
            print("Jij heb iets fouts getyped")
    else:
        print("Jij heb of iets fouts getyped of jij bent niet toegestaan voor een sollicitatie gesprek")
else:
    print("Jij heb of iets fouts getyped of jij bent niet toegestaan voor een sollicitatie gesprek")