from kps import KPS

class KPSPelaajaVsPelaaja(KPS):
    def _kysy_ensimmaisen_siirto(self):
        return input("Ensimmäisen pelaajan siirto: ")

    def _kysy_toisen_siirto(self):
        return input("Toisen pelaajan siirto: ")
