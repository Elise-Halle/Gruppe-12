while True:
    poeng = 0
    print("""
==============================================================================
                        DEN DIGITALE MEDBORGERPORTALEN
==============================================================================

Det har gått seks uker siden Erling, prosjektleder for kommunens nye digitale
medborgerportal, samlet prosjekteammet for første gang.

Teamer består av:
- Erling: Prosjektleder
- Elias: IT-rådgiver
- Silje: UX/UI designer
- Hamdi: Representant fra kulturavdelingen
- Marcia: Politisk rådgiver
- Noa: Sikkerhetsekspert
- Hallgeir: Brukerrepresentant

I starten var motivasjonen høy. Alle ønsket å lage en portal som kunne øke
innbyggerengasjementet og transparensen i kommunen.

Nå har prosjektet gått inn i storming-fasen. Ulike faglige perspektiver
kolliderer og kommunikasjonen blir vanskeligere.

Erling må ta noen viktige beslutninger. Valgene hans vil påvirke både
samarbeidet og prosjektets endelige resultat.
""")
    print("""
==============================================================================

SITUASJON 1. KONFLIKTEN MELLOM SILJE OG ELIAS

Uenigheten om teknologi og design har utviklet seg fra en sakskonflikt til
en personkonflikt.

Silje mener Elias' tekniske løsning vil begrense brukeropplevelsen og hindre innovasjon.

Elias mener Siljes forslag er urealistisk, usikkert og for kostbart.

Diskusjonene blir stadig mer emosjonelle, og begge begynner å trekke støtte fra andre i teamet.

Erling må bestemme hvordan han skal håndtere konflikten.

A) Snakke med silje og Elias individuelt først, og deretter samle dem til et struktuert møte.
   De skal avklare problemene, diskutere prosjektetes krav og vurdere alternative løsninger sammen.

B) Ignorere konflikten og håpe at de løser den selv.
    
""")

    while True:
        svar = input("Velg A eller B: ").upper()
        if svar == "A":
            poeng += 1
            break
        elif svar == "B":
            break
        else:
            print("Ugyldig svar. Skriv A eller B.")

    print("""
==============================================================================

SITUASJON 2. DEN ULMENDE KONFLIKTEN

Samtidig oppstår det spenning mellom Hamdi og Hallgeir. De er uenige om hvordan innbyggerne
skal delta i digitale folkemøter.

Hamdi ønsker en kontrollert løsning gjennom kommunens eksisterende platform.

Hallgeir ønsker et åpent, dialogbasert system med rom for spontane innspill.

Foreløpig er uenigheten en sakskonflikt, men Erling merker at frustrasjonen vokser.

En for kontrollert løsning kan svekke innbyggerdialogen. En for åpen løsning kan skape
utfordringer med moderering, personvern og gjennomføring.

Hva bør Erling gjøre?

A) Invitere Hamdi og Hallgeir til en struktuert samtale, undersøke alternativer og vurdere dem
   etter felles kriterier. Fastsette en frist for beslutningen.

B) Velge Hallgeirs forslag uten å ta hensyn til Hamdis innvendinger.

""")

    while True:
        svar = input("Velg A eller B: ").upper()
        if svar == "A":
            poeng += 1
            break
        elif svar == "B":
            break
        else:
            print("Ugyldig svar. Skriv A eller B.")

    print("""
==============================================================================

SITUASJON 3. TIDSPRESS OG MØTETRØTTHET

Prosjektet er nå halvveis i den tilgjengelige arbeidsperioden.

Teamet føler et stadig større tidspress og ønsker raskere beslutninger.
Medlemmene er lei av møter som tar for mye tid og energi.

Erling må finne en måte å bevare motivasjonen og sikre fremdriften på.

A) Presse teamet til å jobbe raskere uten å endre arbeidsmåten. Beholde alle planlagte møter og
   kreve tettere rapportering.

B) Gjøre møtene kortere og mer målrettede. Involvere teamet i organiseringen, dele arbeidet
   inn i mindre delmål og anerkjenne fremgangen.

""")

    while True:
        svar = input("Velg A eller B: ").upper()
        if svar == "A":
            break
        elif svar == "B":
            poeng += 1
            break
        else:
            print("Ugyldig svar. Skriv A eller B.")

    print(f"""
==============================================================================

Dine poeng: {poeng}""")

    if poeng == 3:
        print("""
POSITIVT UTFALL

Erling håndeterer konfliktene gjennom åpen komunikasjon, strukturert problemløsning og
god oppfølging av teamets behov.

Teamet utvikler en hybridløsning: et moderert dialogrom på kommunens eksisterende platform,
med mulighet for spontane innspill innenfor tydelige rammer for personvern og moderering.

Løsningen ombinerer Siljes fleksible brukeropplevelse med Elias' krav til sikkerhet og kostnadkontroll.

Da tidspresset øker, tilpasser Erling arbeidsmåten og gir teamet større ansvar.

Gruppen utvikler felles normer for samarbeid, gjensidig tillit og god kommunikasjon. Den beveger
seg fra storming-fasen til norming-fasen.

Prototypen leveres i tide og blir godt mottatt av kommunens ledelse.
""")
    elif poeng == 2:
        print("""
NØYTRALT UTFALL

Konfliktene blir hovedsakelig håndtert, og samarbeidet fungerer på et grunnleggende nivå.

Der Erling lytter og bruker struktuerte løsninger, blir stemningen bedre ogg beslutningene tas raskere.

Likevel er motivasjonen lavere enn den kunne ha vært. Noen teammedlemmer føler seg ikke fullt ut
hørt, og fellesskapet er forstatt svakt.

Gruppen befinner seg mellom storming- og norming-fasen.

Prototypen leveres til fristen, men med færre funskjoner enn planlagt. Kvliteten er akseptabel,
men ikke optimal.

Erling må fortsette å følge opp relasjoner og motivasjon.
""")
    else:
        print("""
NEGATIVT UTFALL

Erling klarer ikke å håndtere konfliktene på en tilfredsstillende måte.

Uenighetene forsterkes, og flere teammedlemmer begynner å trekke støtte fra hverandre.
Gruppen deller seg i leirer.

Flere opplever at Erling ikke lytter til ulike faglige perspektiver før han tar beslutninger.

Motivasjonen fller, tidspresset øker, og møtetrøttheten forsterker frustrasjonen.

Informasjonsflyten svikter, og viktige avklaringer blir utsatt eller gjort uten
tilstrekkelig forankring.

Problemer med moderering, personvern og gjennomføring oppdages for sent.

Prototypen blir forsinket og holder lavere kvalitet enn planlagt. Teamet blir stående fast i
storming-fasen, tilliten til Erling svekkes, og prosjektet risikerer å bli forlatt.
""")

    while True:
        svar = input("\nVil du spille en gang til? (Ja/Nei): ").upper()

        if svar in ("JA", "NEI"):
            break
        else:
            print("Ugyldig svar. Skriv Ja eller Nei.")

    if svar == "NEI":
        print("\nTakk for at du spilte!")
        break
