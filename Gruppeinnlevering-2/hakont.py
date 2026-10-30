"""
DEN DIGITALE MEDBORGERPORTALEN
--------------------------------
Interaktivt terminalspill - IS-118 Gruppeinnlevering 2

Leseren folger prosjektleder Erling gjennom tre beslutninger i
storming-fasen. Hvert valg gir 0 eller 1 poeng, og den endelige
poengsummen (0-3) avgjor hvilket utfall historien ender i.
"""

while True:
    poeng = 0

    print("""
==============================================================================
                        DEN DIGITALE MEDBORGERPORTALEN
==============================================================================

Erling leder prosjektet for kommunens nye digitale medborgerportal.

Teamet:
- Erling: Prosjektleder
- Elias:  IT-radgiver
- Silje:  UX/UI-designer
- Hamdi:  Kulturavdelingen
- Marcia: Politisk radgiver
- Noa:    Sikkerhetsekspert
- Hallgeir: Brukerrepresentant

Prosjektet er na i storming-fasen. Erling ma ta tre valg som avgjor
hvordan samarbeidet og prosjektet gar videre.
""")

    # ------------------------------------------------------------------
    # Steg 1: Konflikten mellom Silje og Elias
    # ------------------------------------------------------------------
    print("""
==============================================================================
STEG 1: SILJE OG ELIAS
==============================================================================

Silje og Elias krangler om losningen. Silje mener Elias' forslag
begrenser brukeropplevelsen. Elias mener Siljes forslag er for dyrt
og usikkert. Begge henter stotte fra resten av teamet.

A) Snakk med dem hver for seg, og samle dem til et felles mote. (1 poeng)
B) Ignorer konflikten. (0 poeng)
""")

    while True:
        valg = input("Velg A eller B: ").strip().upper()
        if valg == "A":
            poeng += 1
            break
        elif valg == "B":
            break
        else:
            print("Ugyldig svar. Skriv A eller B.")

    # ------------------------------------------------------------------
    # Steg 2: Uenigheten mellom Hamdi og Hallgeir
    # ------------------------------------------------------------------
    print("""
==============================================================================
STEG 2: HAMDI OG HALLGEIR
==============================================================================

Hamdi og Hallgeir er uenige om folkemotene. Hamdi vil bruke kommunens
egen plattform. Hallgeir vil ha en mer apen losning.

A) Sett en frist, og la dem diskutere losninger sammen. (1 poeng)
B) Velg Hallgeirs forslag uten videre diskusjon. (0 poeng)
""")

    while True:
        valg = input("Velg A eller B: ").strip().upper()
        if valg == "A":
            poeng += 1
            break
        elif valg == "B":
            break
        else:
            print("Ugyldig svar. Skriv A eller B.")

    # ------------------------------------------------------------------
    # Steg 3: Motivasjon, tidspress og motetrotthet
    # ------------------------------------------------------------------
    print(f"""
==============================================================================
STEG 3: TIDSPRESS
==============================================================================

Din poengsum sa langt: {poeng}

Teamet er slitne av moter og vil ha raskere fremgang.

A) Press pa, og krev tettere rapportering. (0 poeng)
B) Kutt moter, og del opp arbeidet sammen med teamet. (1 poeng)
""")

    while True:
        valg = input("Velg A eller B: ").strip().upper()
        if valg == "A":
            break
        elif valg == "B":
            poeng += 1
            break
        else:
            print("Ugyldig svar. Skriv A eller B.")

    # ------------------------------------------------------------------
    # Utfall
    # ------------------------------------------------------------------
    print(f"""
==============================================================================
Din endelige poengsum: {poeng} / 3
==============================================================================""")

    if poeng == 3:
        print("""
POSITIVT UTFALL - Mot norming-fasen

Erling loser begge konfliktene gjennom apen dialog, og teamet finner
gode kompromisser. Da tidspresset oker, tilpasser han arbeidsmaten.
Tilliten i teamet vokser, og prototypen leveres i tide.
""")
    elif poeng == 2:
        print("""
NOYTRALT UTFALL - Fortsatt sarbart samarbeid

Konfliktene blir delvis lost, men ikke alle foler seg hort.
Teamet holder fremdriften, men motivasjonen er lavere enn onsket.
Prototypen leveres, men med faerre funksjoner enn planlagt.
""")
    else:
        print("""
NEGATIVT UTFALL - Konfliktene svekker prosjektet

Uenighetene forsterkes, og tilliten til Erling synker. Viktige
avklaringer blir utsatt. Prototypen blir forsinket og holder
lavere kvalitet enn planlagt.
""")

    while True:
        svar = input("Vil du spille en gang til? (Ja/Nei): ").strip().upper()
        if svar in ("JA", "NEI"):
            break
        print("Ugyldig svar. Skriv Ja eller Nei.")

    if svar == "NEI":
        print("\nTakk for at du spilte!")
        break
