def Konfliktspill():

    print("\nSilje og Elias er uenige om design og teknologi.\nUenigheten har utviklet seg til en personkonflikt, og Erling må bestemme hvordan konflikten skal håndteres.\n")

    print("Hva skal Erling velge å gjøre?\n\n")

    print("A) Erling kaller inn til fellesmøte.\n")
    print("B) Erling tar individuelle samtaler med Silje og Elias.\n\n")

    svar = input("Velg A eller B: ").upper()
    score = 0


    #her sjekker vi om brukeren har valgt A eller B og gir poeng ut fra valget.
    if svar == "A":
        print("\nBegge får fram sin mening og temperaturen synker, de tolererer hverandre greit, men har ennå ikke kommet helt fram til en løsning.\n\n")
        score += 1

        print("Videre får Erling to nye valg for hvordan han skal håndtere konflikten videre :\n\n")
        print("A) Erling passer godt på at alle har fått delt sin side slik vi kan komme til bunns i saken og hvor problemet faktisk ligger.\n")
        print("B) Erling gir dem tre dager for å se om ting har roet seg. Hvis konflikten fortsatt er aktiv, setter han opp et nytt møte.\n\n")

        svar = input("Velg A eller B: ").upper()

        #her nester vi en if statement for å sjekke det neste valget brukeren gjør og gir poeng ut fra det.
        if svar == "A":
            print("\nBegge parter føler seg hørt og forstått, nå gjenstår det bare å finne løsningen.\n\n")
            score += 1

            
            print("Til slutt står Erling overfor disse to siste valgene :\n")
            print("A) Erling passer på at begge sider lager kompromisser slik at ingen går ut av konflikten under den andre og følger opp om en uke.\n")
            print("B) Erling føler at han har gjort sin jobb og at det ordner seg fint herfra.\n\n")

            svar = input("Velg A eller B: ").upper()

            
            if svar == "A":
                print("Konflikten ble løst og Silje og Elias jobber fint i lag.\n\n")
                score += 1
            elif svar == "B":
                print("Silje føler at hun måtte inngå flere kompromisser enn Elias, og føler seg ikke hørt.\n\n")
                
            else:
                    print("Skriv inn A eller B neste gang")

        #her er da B altså den if statmenten som har blitt nestet 1 gang

        elif svar == "B":
            print("\nSilje følte seg ikke helt hørt og det gjorde slik at de ikke klarte å komme til en god løsning.")

            print("Til slutt står Erling overfor disse to siste valgene :\n")
            print("A) Erling setter opp nytt møte der alle skal få rom til å snakke og dele sin mening før han sender dem av gårde til å komme fram til et kompromiss.\n")
            print("B) Erling synes at de har fått nok hjelp og at voksne mennesker burde klare å håndtere resten selv.\n\n")
    
            svar = input("Velg A eller B: ").upper()

            
            if svar == "A":
                print("Begge parter følte seg sett, men de strevde fortsatt med å komme til en god løsning der alle kom ut lykkelige.\n\n")
                score += 1
            elif svar == "B":
                print("Silje og Elias føler seg ikke helt hørt, men konflikten ble for det meste løst.\n\n")
                
            else:
                    print("Skriv inn A eller B neste gang")
        else:
                print("Skriv inn A eller B neste gang")
        

    #her kommer B delen av oppgaven, den er helt lik som A delen, men med andre poeng og print statements.
    elif svar == "B":
        print("\nBegge får fram sin mening, men siden det allerede har blitt en personkonflikt så vil de ikke prate sammen uten andre til stede.\n")
        

        print("videre får Erling to nye valg for hvordan han skal håndtere konflikten videre :\n\n")
        print("A) Erling kaller til gruppemøte slik begge partene får rom til å snakke med tilskuer som kan passe på at det holder seg saklig.\n")
        print("B) Erling tar dem inn på et grupperom for så å dele hva han synes er den beste løsningen.\n\n")

        svar = input("Velg A eller B: ").upper()

        #her nester vi en if statement for å sjekke det neste valget brukeren gjør og gir poeng ut fra det.
        if svar == "A":
            print("\nDet skjer framgang, og de har en grei samtale som kommer seg nærmere en løsning.\n")
            score += 1

            print("Til slutt står Erling overfor disse to siste valgene :\n")
            print("A) Erling passer godt på at alle får delt sin mening.")
            print("B) Erling lar dem diskutere fritt uten å styre samtalen.")
            svar = input("Velg A eller B: ").upper()

            
            if svar == "A":
                print("Det skjer framgang, og de kommer nærmere en løsning.\n\n")
                score += 1
            elif svar == "B":
                print("Diskusjonen blir igjen preget av uenigheter, og de kommer seg ikke lenger.\n\n")
                
            else:
                    print("Skriv inn A eller B neste gang")
            

        # her er da B altså den if statementen som har blitt nestet 1 gang
        elif svar == "B":
            print("\nSilje og Elias føler seg ikke hørt, og konflikten er fortsatt ikke løst.")
            

            print("Til slutt står Erling overfor disse to siste valgene :\n")
            print("A) Erling ser at det fortsatt er uenighet og velger å høre på begge partene.")
            print("B) Erling  tar dem inn på et grupperom og deler hva han mener er den beste løsningen.")
            svar = input("Velg A eller B: ").upper()

            
            if svar == "A":
                print("Silje og Elias føler at meningene deres blir tatt mer på alvor, men det tok for lang tid.\n\n")
                score += 1
            elif svar == "B":
                print("Silje og Elias føler seg overkjørt, konflikten forblir uløst og motivasjonen deres svekkes.\n\n")
                
            else:
                    print("Skriv inn A eller B neste gang")

    #her gir vi kommentar til brukeren om at de må skrive inn A eller B neste gang.
    else:
        print("Skriv inn A eller B neste gang")
    

    if score == 0:
        print(f"Du fikk {score} poeng.")
        print("Konflikten forverres, og påvirker både fremdrift og motivasjon i prosjektet.\n")
    elif score == 1 or score == 2:
        print(f"Du fikk {score} poeng.")
        print("Noen av tiltakene har effekt, men uenigheten er ikke fullstendig løst. Samarbeidet er fortsatt noe anspent.\n")
    elif score == 3:
        print(f"Du fikk {score} poeng.")
        print("Konflikten blir løst, Silje og Elias samarbeider godt og prosjektet går videre som planlagt.\n")
    else:
        print(f"Du fikk {score} poeng.")
        print ("What?!?! Hvordan har du ikke score fra 0-3?!?!\n")


Konfliktspill()