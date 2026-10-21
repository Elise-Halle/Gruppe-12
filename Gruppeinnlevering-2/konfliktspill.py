def Konfliktspill():

    print("Silje og Elias er uenige om design og teknologi. Uenigheten har utviklet seg til en personkonflikt, og erling må bestemme hvordan konflikten skal håndteres.")

    svar = input("Velg A eller B: ").upper()
    score = 0


    # Her er if statement i if statement i if statement. ikke fint

    #her sjekker vi om brukeren har valgt A eller B og gir poeng utifra valget.
    if (svar == "A"):
        print("A")
        score += 1
        svar = input("Velg A eller B: ").upper()

        #her nester vi en if statement for å sjekker det neste valget brukeren gjør og gir poeng utifra det.
        if (svar == "A"):
            print("AA")
            score += 1
            svar = input("Velg A eller B: ").upper()

            #her nester vi enda en if statement i en if statement i en if statement, vakkert
            if (svar == "A"):
                print("AAA")
                score += 1
            elif (svar == "B"):
                print("AAB")
                score += 0

        # her er da B altso den if statmenten som har blitt nestet 1 gang
        elif (svar == "B"):
            print("AB")
            score += 0
            svar = input("Velg A eller B: ").upper()

            #if statement i if statement i if statement
            if (svar == "A"):
                print("ABA")
                score += 1
            elif (svar == "B"):
                print("ABB")
                score += 0
            
        

    #her kommer B delen av oppgaven, den er helt lik som A delen, men med andre poeng og print statements.
    elif (svar == "B"):
        print("B")
        score += 0
        svar = input("Velg A eller B: ").upper()

        #her nester vi en if statement for å sjekker det neste valget brukeren gjør og gir poeng utifra det.
        if (svar == "A"):
            print("BA")
            score += 1
            svar = input("Velg A eller B: ").upper()

            #her nester vi enda en if statement i en if statement i en if statement
            if (svar == "A"):
                print("BAA")
                score += 1
            elif (svar == "B"):
                print("BAB")
                score += 0
            

        # her er da B altso den if statmenten som har blitt nestet 1 gang
        elif (svar == "B"):
            print("BB")
            score += 0
            svar = input("Velg A eller B: ").upper()

            #her nester vi enda en if statement i en if statement i en if statement
            if (svar == "A"):
                print("BBA")
                score += 1
            elif (svar == "B"):
                print("BBB")
                score += 0
            
        
    

    #her gir vi kommentar til brukeren om at de må skrive inn A eller B neste gang.
    else:
        print("Skriv inn A eller B neste gang")
    


    print(f"Du fikk {score} poeng.")

Konfliktspill()