
while True:
    poeng = 0

    print("""
==================================================
       DEN DIGITALE MEDBORGERPORTALEN
==================================================

Det har gått seks uker siden Erling, prosjektleder
for kommunens nye digitale medborgerportal, samlet
prosjektteamet for første gang.

Teamet består av:
- Erling: Prosjektleder
- Elias: IT-rådgiver
- Silje: UX/UI-designer
- Hamdi: Representant fra kulturavdelingen
- Marcia: Politisk rådgiver
- Noa: Sikkerhetsekspert
- Hallgeir: Brukerrepresentant

I starten var motivasjonen høy. Alle ønsket å lage
en portal som kunne øke innbyggerengasjementet og
transparensen i kommunen.

Nå har prosjektet gått inn i storming-fasen.
Ulike faglige perspektiver kolliderer og kommunikasjonen
blir vanskeligere.

Erling må ta noen viktige beslutninger.
Valgene hans vil påvirke både samarbeidet og
prosjektets endelige resultat.
==================================================
""")

    # SITUASJON 1
    print("""
SITUASJON 1: KONFLIKTEN MELLOM SILJE OG ELIAS

Uenigheten om teknologi og design har utviklet seg
fra en sakskonflikt til en personkonflikt.

Silje mener Elias' tekniske løsning vil begrense
brukeropplevelsen og hindre innovasjon.

Elias mener Siljes forslag er urealistisk, usikkert
og for kostbart.

Diskusjonene blir stadig mer emosjonelle, og begge
begynner å trekke støtte fra andre i teamet.

Erling må bestemme hvordan han skal håndtere konflikten.

A) Snakke med Silje og Elias individuelt først,
   og deretter samle dem til et strukturert møte.
   De skal avklare problemene, diskutere prosjektets
   krav og vurdere alternative løsninger sammen.

B) Ignorere konflikten og håpe at de løser den selv.
""")

    while True:
        svar = input("Velg A eller B: ").upper()

        if svar == "A":
            poeng += 1
            print("""
Erling snakker først med begge individuelt.
Deretter samler han dem til et strukturert møte.

De definerer felles mål og vurderingskriterier,
presenterer argumentene sine og undersøker
alternative løsninger.

Erling avtaler regler for videre samarbeid og
følger opp relasjonene etter møtet.

Ved å bruke diskursiv kommunikasjon forsøker han
å avklare problemstillingen og finne frem til
en felles forståelse. Dette er i tråd med strategi 1.

Konflikten dempes, og teamet kan konsentrere seg
om prosjektets mål.
""")
            break

        elif svar == "B":
            print("""
Erling unngår å gripe inn.

Silje og Elias fortsetter å være uenige, og begge
trekker støtte fra andre teammedlemmer.

Prosjektgruppen begynner å dele seg i leirer.
Fremdriften svekkes, og arbeidsmiljøet forverres.

En uløst sakskonflikt har utviklet seg til en
sterkere personkonflikt.
""")
            break

        else:
            print("Ugyldig svar. Skriv A eller B.")

    # SITUASJON 2
    print("""
SITUASJON 2: DEN ULMENDE KONFLIKTEN

Samtidig oppstår det spenning mellom Hamdi og
Hallgeir. De er uenige om hvordan innbyggerne
skal delta i digitale folkemøter.

Hamdi ønsker en kontrollert løsning gjennom
kommunens eksisterende plattform.

Hallgeir ønsker et åpent, dialogbasert system
med rom for spontane innspill.

Foreløpig er uenigheten en sakskonflikt, men
Erling merker at frustrasjonen vokser.

En for kontrollert løsning kan svekke
innbyggerdialogen. En for åpen løsning kan skape
utfordringer med moderering, personvern og
gjennomføring.

Hva bør Erling gjøre?

A) Invitere Hamdi og Hallgeir til en strukturert
   samtale, undersøke alternativer og vurdere dem
   etter felles kriterier. Fastsette en frist for
   beslutningen.

B) Velge Hallgeirs forslag uten å ta hensyn til
   Hamdis innvendinger.
""")

    while True:
        svar = input("Velg A eller B: ").upper()

        if svar == "A":
            poeng += 1
            print("""
Erling inviterer Hamdi og Hallgeir til en
strukturert samtale.

De vurderer alternativene opp mot prosjektets mål,
innbyggernes behov, personvern og moderering.

Erling oppmuntrer til åpen kommunikasjon og
forsøker først å oppnå konsensus.

Samtidig setter han en frist for beslutningen.
Dersom de ikke blir enige, kan han bruke tydeligere
regler, kompromiss eller en flertallsbeslutning.

Dette kombinerer samarbeid med behovet for fremdrift.
""")
            break

        elif svar == "B":
            print("""
Erling velger Hallgeirs forslag uten å vurdere
Hamdis innvendinger.

Hamdi mister motivasjonen og blir mindre villig
til å samarbeide.

Andre teammedlemmer begynner å tvile på om Erling
tar hensyn til ulike faglige perspektiver.

Utfordringer med moderering, personvern og
gjennomføring kan oppstå senere.
""")
            break

        else:
            print("Ugyldig svar. Skriv A eller B.")

    # SITUASJON 3
    print("""
SITUASJON 3: TIDSPRESS OG MØTETRØTTHET

Prosjektet er nå halvveis i den tilgjengelige
arbeidsperioden.

Teamet føler et stadig større tidspress og ønsker
raskere beslutninger. Medlemmene er lei av møter
som tar for mye tid og energi.

Den første prototypen skal fortsatt leveres
om tre uker.

Erling må finne en måte å bevare motivasjonen
og sikre fremdriften på.

A) Presse teamet til å jobbe raskere uten å endre
   arbeidsmåten. Beholde alle planlagte møter og
   kreve tettere rapportering.

B) Gjøre møtene kortere og mer målrettede.
   Involvere teamet i organiseringen, dele arbeidet
   inn i mindre delmål og anerkjenne fremgangen.
""")

    while True:
        svar = input("Velg A eller B: ").upper()

        if svar == "A":
            print("""
Erling legger større vekt på fristen enn på
teamets frustrasjon.

Han beholder møtestrukturen, øker kontrollen med
fremdriften og krever hyppigere rapportering.

Teamet opplever mindre handlingsrom, og
møtetrøttheten kan forsterkes.
""")
            break

        elif svar == "B":
            poeng += 1
            print("""
Erling lytter til teamets frustrasjon og tar
den på alvor.

Han kutter unødvendige møter, gir de resterende
møtene tydelige agendaer og deler arbeidet inn
i mindre delmål.

Teammedlemmene får større ansvar for egne områder.
Erling anerkjenner innsatsen og markerer oppnådde
delmål.

Dette styrker opplevelsen av eierskap og mestring,
samtidig som prosjektet beholder fremdriften.
""")
            break

        else:
            print("Ugyldig svar. Skriv A eller B.")

    # RESULTAT
    print("\n" + "=" * 50)
    print(f"Resultat: Du fikk {poeng} av 3 poeng.")
    print("=" * 50)

    if poeng == 3:
        print("""
POSITIVT UTFALL

Erling håndterer konfliktene gjennom åpen
kommunikasjon, strukturert problemløsning og
god oppfølging av teamets behov.

Teamet utvikler en hybridløsning: et moderert
dialogrom på kommunens eksisterende plattform,
med mulighet for spontane innspill innenfor
tydelige rammer for personvern og moderering.

Løsningen kombinerer Siljes fleksible
brukeropplevelse med Elias' krav til sikkerhet
og kostnadskontroll.

Da tidspresset øker, tilpasser Erling
arbeidsmåten og gir teamet større ansvar.

Gruppen utvikler felles normer for samarbeid,
gjensidig tillit og god kommunikasjon. Den beveger
seg fra storming-fasen til norming-fasen.

Prototypen leveres i tide og blir godt mottatt
av kommunens ledelse.
""")

    elif poeng == 2:
        print("""
NØYTRALT UTFALL

Konfliktene blir hovedsakelig håndtert, og
samarbeidet fungerer på et grunnleggende nivå.

Der Erling lytter og bruker strukturerte løsninger,
blir stemningen bedre og beslutningene tas raskere.

Likevel er motivasjonen lavere enn den kunne ha
vært. Noen teammedlemmer føler seg ikke fullt ut
hørt, og fellesskapet er fortsatt svakt.

Gruppen befinner seg mellom storming- og
norming-fasen.

Prototypen leveres til fristen, men med færre
funksjoner enn planlagt. Kvaliteten er akseptabel,
men ikke optimal.

Erling må fortsette å følge opp relasjoner
og motivasjon.
""")

    else:
        print("""
NEGATIVT UTFALL

Erling klarer ikke å håndtere konfliktene
på en tilfredsstillende måte.

Uenighetene forsterkes, og flere teammedlemmer
begynner å trekke støtte fra hverandre.
Gruppen deler seg i leirer.

Flere opplever at Erling ikke lytter til ulike
faglige perspektiver før han tar beslutninger.

Motivasjonen faller, tidspresset øker, og
møtetrøttheten forsterker frustrasjonen.

Informasjonsflyten svikter, og viktige avklaringer
blir utsatt eller gjort uten tilstrekkelig
forankring.

Problemer med moderering, personvern og
gjennomføring oppdages for sent.

Prototypen blir forsinket og holder lavere kvalitet
enn planlagt. Teamet blir stående fast i
storming-fasen, tilliten til Erling svekkes,
og prosjektet risikerer å bli forlatt.
""")

    # SPILL PÅ NYTT
    while True:
        svar = input(
            "\nVil du spille en gang til? (Ja/Nei): "
        ).upper()

        if svar in ("JA", "NEI"):
            break

        print("Ugyldig svar. Skriv Ja eller Nei.")

    if svar == "NEI":
        print("\nTakk for at du spilte!")
        break
    