class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.edellinen = 0

    def miinus(self, arvo):
        self.paivita_edellinen()

        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.paivita_edellinen()
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.paivita_edellinen()
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.paivita_edellinen()
        self.tulos = arvo

    def paivita_edellinen(self):
        self.edellinen = self.tulos