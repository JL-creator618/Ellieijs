from algemene_functies import mijn_functie2


def aanbieding_1(smaak, prijs,korting):
    prijs_na_korting = prijs - (prijs*korting)
    korting = float(korting)
    uitvoer_tekst = f"Vandaag in de aanbieding : emmertje ijs (1 liter) in de smaak {smaak} van {prijs} euro voor {prijs_na_korting:.2f} euro."
    return uitvoer_tekst


def inkomst_totaal (inkomsten, btw):
    totaal_week = sum(inkomsten)
    btw_in_euro = totaal_week * btw
    uitvoer_tekst = f"Het totaal van alle inkmosten van deze week {totaal_week} euro waarover {btw_in_euro:.2f} euro btw betaald dient te worden." 
    return uitvoer_tekst


def laag_hoog (mijn_lijst):
    return (max(mijn_lijst), min(mijn_lijst))


def gemiddelde(mijn_lijst):
    gem_bedrag = (sum (mijn_lijst)/ len (mijn_lijst))
    uitvoer_tekst = f"De gemiddelde inkomsten deze week zijn {gem_bedrag:.2f} euro"
    return uitvoer_tekst 


def meervoudig (invoer_lijst):
    uitvoer = laag_hoog (invoer_lijst)
    return uitvoer


def combinatie (invoer_lijst_2):
    korte_lijst = laag_hoog (invoer_lijst_2)
    uitvoer = mijn_functie2 (korte_lijst [0],korte_lijst [1])
    return uitvoer


