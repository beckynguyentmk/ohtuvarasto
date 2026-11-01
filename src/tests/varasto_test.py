import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_ei_luo_negatiivista_saldoa(self):
        var=Varasto(10,-1)
        self.assertAlmostEqual(var.saldo,0)

    def test_luo_oikean_saldon(self):
        var=Varasto(10,3)
        self.assertAlmostEqual(var.saldo,3)

    def test_ei_luo_ylimääräistä_saldoa(self):
        var=Varasto(10,20)
        self.assertAlmostEqual(var.saldo,10)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_ei_luo_negatiivista_tilavuutta(self):
        var=Varasto(-1)
        self.assertAlmostEqual(var.tilavuus,0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_ei_lisaa_negatiivista_maara(self):
        var=Varasto(10,3)
        var.lisaa_varastoon(-1)
        self.assertAlmostEqual(var.saldo,3)

    def test_lisays_ei_ylita_tilavuutta(self):
        var=Varasto(10,3)
        var.lisaa_varastoon(18)
        self.assertAlmostEqual(var.saldo,10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaa_saattavilla_olevan_maaran(self):
        var=Varasto(10,3)
        saatu_maara=var.ota_varastosta(4)
        self.assertAlmostEqual(saatu_maara,3)

    def test_ei_ota_negatiivista_maara(self):
        var=Varasto(10,3)
        saatu_maara=var.ota_varastosta(-1)
        self.assertAlmostEqual(saatu_maara,0)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)
