poeng=0

#--------Valg Kode---------
def valg (valg_a, valg_b):
    poeng=0
    while (True):
        svar = input ("A eller B?").upper()
        if (svar == "A"):
            print (f"Du velger å {valg_a}")
            poeng += 1
            break
        elif (svar == "B"):
            print (f"du velger å {valg_b}")
            break
        else:
            print ("ugyldig svar. Skriv inn A eller B")
    return poeng


#--------Introduksjon----------
print ("Velkommen! I dette spillet skal du ta noen valg som en prosjektleder. Basert på dine valg vil du få forskjellige poeng som fører til forksjellige slutter. For å komme videre til neste steg klikk enter.")
input ()

#----------Konflikt 1----------
print ("En konflikt mellom Silje og Elias starter,")
print ("I starten var stemningen god. Gruppen opplevde høy motivasjon og fellesskap i måletom å lage en portal som kunne øke innbyggerengasjement og transparens i kommunen. Men nå, etter seks uker, har prosjektet gått inn i den klassiske storming-fasen, der ulike faglige perspektiver og personlige preferanser begynner å kollidere")
input ()
print ("Uenighet om teknologivalg og design har utviklet seg fra en sakskonflikt til en personkonflikt. Silje mener løsningen Elias foreslår vil låse brukeropplevelsen og hindre innovasjon. Elias mener Siljes forslag er urealistisk, usikkert og for kostbart. Diskusjonene blir stadig mer emosjonelle, og begge trekker støtte fra sine nærmeste i teamet.")
input ()
print ("Skal du som prosjektleder:")
print ("A = Ta individuelle samtaler med Silje og Elias")
print ("B = Ignorere konflikten å unngå å ta beslutninger?")

valg ("ta individuelle samtaler. Ved å ta det opp med de det gjelder så blir ikke konflikten større enn nødvendig. Det bygger også tillit til prosjektleder sin makt samtidig som begge parter kan føle at de blir hørt", "ignorere konflikten og unngår å ta beslutninger. Dette fører til at konflikter blir større og ender opp med at Elias trekker seg ut av gruppa. Siden du som prosjektleder ikke tok et valg mistet alle tilliten til deg som leder og motivasjonen minskes.")
input ()

#--------Konflikt 2-----------
print ("Samtidig med konflikten mellom Silje og Elias oppstår det spenning mellom Hamdi (kulturavdelingen) og Hallgeir (brukerrepresentant).")
input ()
print ("De er uenige om hvordan innbyggerne skal kunne delta i digitale folkemøter: Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende plattform. Hallgeir ønsker et mer åpent, dialogbasert system med rom for spontane innspill.") 
input ()
print ("Skal du som prosjektleder:")
print ("A=Felles møte og drøfte avgjørelsen")
print ("B=Ta et valg som leder å velge Hallgeir sitt forslag")


valg ( "kalle inn til et felles møte å drøfte avgjørelsen sammen med hele gruppa. Begge føler seg hørt samtidig som spenning som har bygget seg løses opp. Alle i gruppa er med på å  brainstorme en ny og bedre konklusjon og økee tilitten de har til deg som prosjektleder.", "ta et valg som leder å belger Hallgeir sitt forslalg. Hamdi føler seg uhørt og nedprioritert og føler at hans kunnskap ikke er viktig. Hamdi sin motivasjon og medvirkelse i gruppa går ned og ødelegge videre for han å ønske å dele faglig kunnskap")
input ()

#----------Konflikt 3----------
print ("Foreløpig er uenigheten lavmælt, men Erling merker at frustrasjonen vokser. Prosjektet nærmer seg en viktig milepæl: første prototype skal være klar om tre uker. Stemningen er spent, kommunikasjonen hakkete, og Erling vet at hans neste valg kan avgjøre om teamet beveger seg videre mot “norming” – eller blir stående fast i stormen")
input ()
print ("Skal du som prosjektleder:")
print ("A = Presse på for å rekke fristen")
print ("B = Endre arbeidsmetode og involvere teamet")

valg ( "endre arbeidsmetode og involvere teamet. Du setter deg ned med gruppa og lar de dele hvordan de føler seg og hva de trenger for å føle seg støttet videre. Dere leverer prosjektet en uke etter fristen, men kvaliteten er høy og gruppa ser på deg som en god prosjektleder.", "presse på for å rekke fristen. Gruppen får levert inn prosjektet i tidet, men kvaliteten er ikke så god som den kunne ettersom gruppa var demotivert. De følte seg ikke hørt og tar det opp videre til HR at du ikke er en god prosjektleder.")
input ()

#----------Resultat----------
print ("Etter valgene du har tatt som prosjekleder, ble dette resultatet av prosjektet:", (poeng), "poeng")

if poeng == 3:
    print ("God slutt")
    print ("Godt jobbet! Du tok de beste valgene som prosjektleder og prosjektet går videre fra storming fasen, til normings fasen. Alle konfliktene ble løst og motivasjonen til gruppen er på sitt høyeste")
elif poeng in (1, 2):
    print ("Nøytral slutt")
    print ("Du tok noen dårlige valg på veien. Konfliktene er delvist løst og ikke alle er fornøyd med valgene som er tatt. Gruppemotivasjonen er nede, men alle jobber videre for å oppnå målet.")
else:
    print ("Dårlig slutt")
    print ("ingen konflikter ble løst og prosjektet blir forsinket. Noen medlemmer ønsker å gå ut av prosjektet og all tillit til deg som prosjektleder er mistet.")
