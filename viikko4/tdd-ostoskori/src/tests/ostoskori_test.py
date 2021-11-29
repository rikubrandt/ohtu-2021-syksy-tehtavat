import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):

        self.kori.lisaa_tuote(Tuote("Maito", 2))
        self.assertEqual(self.kori.tavaroita_korissa(),1)


    def test_lisaa_yksi_tuote_ostoskorilla_sama_hinta_kuin_tuotteella(self):
        maito = Tuote("Maito", 2)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.hinta(), maito.hinta())

    def test_lisaa_kaksi_eri_tuotetta(self):
        maito = Tuote("Maito", 2)
        juusto = Tuote("Juusto", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(juusto)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_lisaa_kaksi_eri_tuotetta_summa(self):
        maito = Tuote("Maito", 2)
        juusto = Tuote("Juusto", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(juusto)
        self.assertEqual(self.kori.hinta(), 5)

    def test_lisaa_kaksi_samaa_tuotetta(self):
        maito = Tuote("Maito", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kaksi_samaa_tuotetta_hinta_sama(self):
        maito = Tuote("Maito", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 4)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
 
        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")