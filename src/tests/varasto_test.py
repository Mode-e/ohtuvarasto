import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_konstruktori_nollaa_vaaran_alkusaldon(self):
        virheellinen_varasto = Varasto(10, -5)
        self.assertAlmostEqual(virheellinen_varasto.saldo, 0.0)

    def test_konstruktori_nollaa_vaaran_tilavuuden(self):
        virheellinen_varasto = Varasto(-10)
        self.assertAlmostEqual(virheellinen_varasto.tilavuus, 0.0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_lisays_lisaa_liian_pienella(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_lisays_lisaa_liian_suurella(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0.0)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(0)
        self.assertAlmostEqual(saatu_maara, 0)

    def test_ottaminen_liian_pienellä_maaralla(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(saatu_maara, 0.0)

    def test_ottaminen_liikaa(self):
        self.varasto.lisaa_varastoon(8)
        saatu_maara = self.varasto.ota_varastosta(9)
        self.assertAlmostEqual(saatu_maara, 8)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_merkkijonoesitys_tulostaa_oikein(self):
        odotettu_teksti = "saldo = 0, vielä tilaa 10"
        self.assertEqual(str(self.varasto), odotettu_teksti)
