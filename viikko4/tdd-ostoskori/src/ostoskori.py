from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.kori = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        if len(self.kori) < 1:
            return 0
        maara = 0
        for ostos in self.kori:
            maara += ostos.lukumaara()
        return maara
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        summa = 0
        for ostos in self.kori:
            summa += ostos.hinta()
        return summa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        tuote = next((i for i, x in enumerate(self.kori) if x.tuote.nimi()==lisattava.nimi()), None)
        if tuote != None:
            t = self.kori[tuote]
            t.muuta_lukumaaraa(1)
        else:
            self.kori.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        tuote = next((i for i, x in enumerate(self.kori) if x.tuote.nimi()==poistettava.nimi()), None)
        o = self.kori[tuote]
        o.muuta_lukumaaraa(-1)


    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.kori
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
