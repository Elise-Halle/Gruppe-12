def Konfliktspill():

    print("\nSilje og Elias er uenige om design og teknologi.\nUenigheten har utviklet seg til en personkonflikt, og Erling må bestemme hvordan konflikten skal håndteres.\n")

    print("Hva skal Erling velge å gjøre?\n\n")

    print("A) Erling kaller inn til fellesmøte.\n")
    print("B) Erling tar individuelle samtaler med Silje og Elias.\n\n")

    svar = input("Velg A eller B: ").upper()
    score = 0


    # Her er if statement i if statement i if statement. ikke fint

    #her sjekker vi om brukeren har valgt A eller B og gir poeng utifra valget.
    if (svar == "A"):
        print("\nbegge får fram sin mening og temperaturen synker, de tolererer hvarandre greit, men har ennå ikke kommet helt framm til en løsning.\n\n")
        score += 1

        print("videre får Erling to til valg for hvordan han skal hondtrere konflikten på videre :\n\n")
        print("A) Erling passer godt på at alle har fått delt sin side slik vi kan komme til bunns i saken og hvor problemet faktisk ligger.\n")
        print("B) Erling gir dem tre dager for å se om ting har roet seg, og dermed konflikten fortsatt er aktiv så setter han opp nytt møte.\n\n")

        svar = input("Velg A eller B: ").upper()

        #her nester vi en if statement for å sjekker det neste valget brukeren gjør og gir poeng utifra det.
        if (svar == "A"):
            print("\nBegge parter føler seg hørt og forstått, nå gjenstår det bare å finne løsningen.\n\n")
            score += 1

            
            print("Til slutt står Erling ovenfor desse to siste valgene :\n")
            print("A) Erling passer på at begge sider lager kompromisser slik at ingen går ut av konflikten under den andre og følger opp om en uke.\n")
            print("B) Erling føler at han har gjort sin jobb og at det ordner seg fint her ifra.\n\n")

            svar = input("Velg A eller B: ").upper()

            #her nester vi enda en if statement i en if statement i en if statement, vakkert
            if (svar == "A"):
                print("Konflikten ble løst og Silje og Elias jobber fint i lag.\n\n")
                score += 1
            elif (svar == "B"):
                print("Silje føler at hun komprimerte mer enn Elias og føler seg ikke hørt.\n\n")
                score += 0
            else:
                    print("Skriv inn A eller B neste gang")

        #her er da B altso den if statmenten som har blitt nestet 1 gang

        elif (svar == "B"):
            print("\nSilje følte seg ikke helt hørt og det gjorde slik att de ikke klarte å komme til en god løsning.")
            score += 0

            print("Til slutt står Erling ovenfor desse to siste valgene :\n")
            print("A) Erling setter opp nytt møte der alle skal få rom til å snakke og dele sin mening før han sender dem avgårde til å komme fram til et kompromiss.\n")
            print("B) Erling synes at de har fått nok hjelp og at voksne mennesker burde klare å håndtere resten selv.\n\n")
    
            svar = input("Velg A eller B: ").upper()

            #if statement i if statement i if statement
            if (svar == "A"):
                print("begge parter følte seg sett, men de strevde fortsatt med å komme til en god løsning der alle kom ut lykkelige.\n\n")
                score += 1
            elif (svar == "B"):
                print("Silje og Elias føler seg ikke helt hørt, men konflikten ble for det meste løst.\n\n")
                score += 0
            else:
                    print("Skriv inn A eller B neste gang")
        else:
                print("Skriv inn A eller B neste gang")
        

    #her kommer B delen av oppgaven, den er helt lik som A delen, men med andre poeng og print statements.
    elif (svar == "B"):
        print("\nBegge får fram sin mening, men siden det allerede har blitt en personkonflikt så vill de ikke prate sammen uten andre til stedet.\n")
        score += 0

        print("videre får Erling to til valg for hvordan han skal hondtrere konflikten på videre :\n\n")
        print("A) Erling kaller til gruppemøte slik begge partene får rom til å snakke med tilskuer som kan passe på at det holder seg saklig.\n")
        print("B) Erling tar dem inn på ett grupper rom for å så dele hva han synest er beste løsningen.\n\n")

        svar = input("Velg A eller B: ").upper()

        #her nester vi en if statement for å sjekker det neste valget brukeren gjør og gir poeng utifra det.
        if (svar == "A"):
            print("\nDet skjer framgang, og de har en grei samtale som kommer seg nærmere en løsning.\n")
            score += 1

            print("Til slutt står Erling ovenfor desse to siste valgene :\n")
            print("A) Erling passer godt på at alle får delt sin mening.")
            print("B) Erling lar dem diskutere fritt uten å styre samtalen.")
            svar = input("Velg A eller B: ").upper()

            #her nester vi enda en if statement i en if statement i en if statement
            if (svar == "A"):
                print("Det skjer framgang, og de kommer nermere en løsning.\n\n")
                score += 1
            elif (svar == "B"):
                print("Diskusjonen blir igjen preget av uenigheter, og de kommer seg ikke lengre.\n\n")
                score += 0
            else:
                    print("Skriv inn A eller B neste gang")
            

        # her er da B altso den if statmenten som har blitt nestet 1 gang
        elif (svar == "B"):
            print("\nSilje og Elias føler seg ikke hørt, og konflikten er fortsatt ikke løst.")
            score += 0

            print("Til slutt står Erling ovenfor desse to siste valgene :\n")
            print("A) Erling ser der fortsatt er uenighet og velger å høre på begge partene.")
            print("B) Erling  tar dem inn på ett grupperom og deler hva han mener er den beste løsningen.")
            svar = input("Velg A eller B: ").upper()

            #her nester vi enda en if statement i en if statement i en if statement
            if (svar == "A"):
                print("Silje og Elias føler at meningene deres blir tatt mer på allvor, men det tok for lang tid.\n\n")
                score += 1
            elif (svar == "B"):
                print("Silje og Elias føler seg overkjørt, konflikten forblir uløst og motivasjonen deres svekkes.\n\n")
                score += 0
            else:
                    print("Skriv inn A eller B neste gang")

    #her gir vi kommentar til brukeren om at de må skrive inn A eller B neste gang.
    else:
        print("Skriv inn A eller B neste gang")
    



    if (score == 0):
        print(f"Du fikk {score} poeng.")
        print("Konflikten forverres, og påvirker både fremdrift og motivasjon i prosjektet.\n")
    elif (score == 1 or score == 2):
        print(f"Du fikk {score} poeng.")
        print("Noen av tiltakene har effekt, men uenigheten er ikke fullstendigt løst. Sammarbeidet er fortsatt noe annspent.\n")
    elif (score == 3):
        print(f"Du fikk {score} poeng.")
        print("Konflikten blir løst, Silje og Elias sammarbeider godt og prosjekter går videre som planlagt.\n")
    else:
        print(f"Du fikk {score} poeng.")
        print ("What?!?! Hvordan har du ikke scor fra 0-3?!?!\n")


Konfliktspill()