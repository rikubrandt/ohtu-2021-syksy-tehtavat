import unittest
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()
        self.maito = Tuote("Maito", 2)
        self.juusto = Tuote("Juusto", 3)

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.tavaroita_korissa(),1)


    def test_lisaa_yksi_tuote_ostoskorilla_sama_hinta_kuin_tuotteella(self):
        self.kori.lisaa_tuote(self.maito)
        self.assertEqual(self.kori.hinta(), self.maito.hinta())

    def test_lisaa_kaksi_eri_tuotetta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.juusto)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_lisaa_kaksi_eri_tuotetta_summa(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.juusto)
        self.assertEqual(self.kori.hinta(), 5)

    def test_lisaa_kaksi_samaa_tuotetta(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kaksi_samaa_tuotetta_hinta_sama(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)

        self.assertEqual(self.kori.hinta(), 4)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        self.kori.lisaa_tuote(self.maito)
 
        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 1)
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
    
        self.kori.lisaa_tuote(self.maito)
 
        ostos = self.kori.ostokset()[0]

        self.assertEqual(ostos.tuotteen_nimi(), "Maito")

    def test_kaksi_eri_tuotetta_ostoskorin_pituus(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.juusto)
        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 2)

    def test_kaksi_samaa_tuotetta_ostoksien_pituus(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)

    def test_sama_tuote_ostoksien_lukumaara(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        ostokset = self.kori.ostokset()
        ostos = ostokset[0]
        self.assertEqual(ostos.lukumaara(), 2)

    def test_kaksi_samaa_tuotetta_poista_toinen(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.kori.poista_tuote(self.maito)
        ostokset = self.kori.ostokset()
        self.assertEqual(ostokset[0].lukumaara(), 1)

    def test_yksi_tuote_poistetaan_kori_tyhja(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.poista_tuote(self.maito)

        ostokset = self.kori.ostokset()
        self.assertEqual(len(ostokset), 0)

    def test_tyhjenna_kori(self):
        self.kori.lisaa_tuote(self.maito)
        self.kori.lisaa_tuote(self.maito)
        self.kori.tyhjenna()

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 0)
        