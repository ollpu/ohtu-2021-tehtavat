from kps import KPS

class KPSPelaajaVsTekoaly(KPS):
    def __init__(self, tekoaly):
        super().__init__()
        self._tekoaly = tekoaly

    def _kysy_ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _kysy_toisen_siirto(self):
        siirto = self._tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {siirto}")
        return siirto

    def _ilmoita_ensimmaisen_siirto(self, siirto):
        self._tekoaly.aseta_siirto(siirto)
