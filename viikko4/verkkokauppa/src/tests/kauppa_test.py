import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 3
            elif tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            elif tuote_id == 2:
                return Tuote(2, "vesi", 9)
            elif tuote_id == 3:
                return TUote(3, "cola", 999)

        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)


    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikein(self):
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu oikein
        self.pankki_mock.tilisiirto.assert_called_with("pekka", 42, "12345", ANY, 5)

    def test_tilisiirto_ostoksista_kahdella_tuotteella(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pätkä", "23456")

        self.pankki_mock.tilisiirto.assert_called_with("pätkä", 42, "23456", ANY, 14)

    def test_tilisiirto_ostoksista_kahdella_samalla_tuotteella(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pouta", "34567")

        self.pankki_mock.tilisiirto.assert_called_with("pouta", 42, "34567", ANY, 10)

    def test_tilisiirto_ostoksista_tuote_loppu(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pertti", "45678")

        self.pankki_mock.tilisiirto.assert_called_with("pertti", 42, "45678", ANY, 5)

    def test_aloita_asiointi_tyhjentää_ostoskorin(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("janne", "56789")

        self.pankki_mock.tilisiirto.assert_called_with("janne", 42, "56789", ANY, 9)

    def test_aloita_asiointi_pyytaa_uuden_viitenumeron(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.tilimaksu("asd", "asd")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)
        self.kauppa.aloita_asiointi()
        self.kauppa.tilimaksu("asd", "asd")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)
        self.kauppa.aloita_asiointi()
        self.kauppa.tilimaksu("asd", "asd")
        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 3)

    def test_poista_korista(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pertti", "67890")

        self.pankki_mock.tilisiirto.assert_called_with("pertti", 42, "67890", ANY, 9)
