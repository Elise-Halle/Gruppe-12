# Problem 1
poeng = 0


print("Det har gått seks uker siden Erling, prosjektleder for utviklingen av kommunens \nnye digitale medborgerportal, samlet sitt prosjektteam for første gang. \nEtter en inspirerende oppstart med høy energi, begynner samarbeidet \nnå å møte sine første reelle prøver.")

print("Silje og Elias er uenige om teknologivalg og design. Diskusjonene har emosjonelle \nog høylytte. Hvordan skal Erling velge å møte konflikten?\n\n")

print("A)Inviter på individuelle samtaler.\n")

print("B)Unngå å ta besluttninger og ignorer konflikten.\n\n")


valg = input("Svar enten A eller B: ")

if valg == "A": #Husk at de kan skrive liten a
    poeng = poeng + 1
else: 
    poeng == poeng



#Problem 2
print("\nSamtidig med konflikten mellom Silje og " \
"Elias oppstår det spenning mellom Hamdi og Hallgeir.\n" \
"De er uenige om hvordan innbyggerne skal kunne delta i digitale\n " \
"folkemøter.Foreløpig er uenigheten lavmælt, men Erling merker at\n " \
"frustrasjonen vokser. Prosjektet nærmer seg en viktig milepæl:\n " \
"første prototype skal være klar om tre uker. Stemningen er spent,\n " \
"kommunikasjonen hakkete, og Erling vet at hans neste valg kan\n " \
"avgjøre om teamet beveger seg videre mot “norming” – eller blir stående fast i stormen\n\n" \
"Elias har to valg:\n" \
"A)  Ta en beslutning og velg hallgeir sitt forslag.\n" \
"B)  Kann inn til felles møte for å drøfte forskjellige løsninger.\n")

valg = input("Svar enten A eller B: ")

if valg == "A": #Husk at de kan skrive liten a
    poeng == poeng 
else: 
    poeng = poeng + 1


print(f"\nDin poengsum sålangt er: {poeng}")


#Problem 3
print("Nå er det kritisk at Erling får motivasjon til teamet som helhet.\n" \
"Hvordan skal ha oppnå dette?\n\n" \
"A) Bare press på, de trenger å få rævva i gir.\n" \
"B) Endre arbeidsmetode og involver teamet i beslutninger\n")

valg = input("Svar enten A eller B: ")

if valg == "A": #Husk at de kan skrive liten a
    poeng == poeng 
else: 
    poeng = poeng + 1


#Resultat
print(f"\nDin endelige poengsum er: {poeng}")

if poeng == 3:
    print("Gratulerer, du har nådd norming-fasen")
elif poeng == 2:
    print("Nøytral slutt. Konfliktene er delvis løst og gruppemotivasjonen er begrensest.")
else:
    print("Uffda, ingen konflikter ble løst og prosjektet blir utsatt.")