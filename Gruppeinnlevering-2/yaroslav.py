while(True):
    poeng = 0
    print("Start.")
    print("Situasjon 1.")
    
    while(True):
        svar = input("Velg A eller B: ").upper()
        if (svar == "A"):
            print(svar)
            poeng += 1
            break
        elif (svar == "B"):
            print ("B")
            break
        else:
            (print("Wrong answer"))

    print("Situasjon 2.")
    
    while(True):
        svar = input("Velg A eller B: ").upper()
        if (svar == "A"):
            print("A")
            poeng += 1
            break
        elif (svar == "B"):
            print ("B")
            break
        else:
            (print("Wrong answer"))

    print("Situasjon 3.")
    
    while(True):
        svar = input("Velg A eller B: ").upper()
        if (svar == "A"):
            print("A")
            break
        elif (svar == "B"):
            print ("B")
            poeng += 1
            break
        else:
            (print("Wrong answer"))

    print(f"Dine poeng er: {poeng}")

    if poeng == 3:
        print("Positivt utfall")
    elif poeng == 2:
        print("Nøytralt utfall")
    else:
        print("Negativt utfall")

    while(True):
        svar = input("Vil du spille en gong til? (Ja/Nei): ").upper()
        if svar in ("JA", "NEI"):
            break
        else:
            print("Feil svar. Bruk Ja eller Nei.")
        
    if svar == "NEI":
        print("Takk for at du spilte!")
        break