KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None:
            self.kapasiteetti = KAPASITEETTI
        elif not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise ValueError("Kapasiteetin on oltava epänegatiivinen kokonaisluku")
        else:
            self.kapasiteetti = kapasiteetti

        if kasvatuskoko is None:
            self.kasvatuskoko = OLETUSKASVATUS
        elif not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise ValueError("Kasvatuskoon on oltava epänegatiivinen kokonaisluku")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.taulukko = [0] * self.kapasiteetti

        self.koko = 0

    def _iteroi_sisalto(self):
        return self.taulukko[:self.koko]

    def _etsi(self, etsittävä):
        for indeksi, luku in enumerate(self._iteroi_sisalto()):
            if luku == etsittävä:
                return indeksi
        return None

    def _kasvata_jonoa(self):
        vanha_kapasiteetti = len(self.taulukko)
        uusi_kapasiteetti = vanha_kapasiteetti + self.kasvatuskoko
        uusi_taulukko = [0]*uusi_kapasiteetti
        for i, luku in enumerate(self._iteroi_sisalto()):
            uusi_taulukko[i] = luku
        self.taulukko = uusi_taulukko

    def kuuluu(self, luku):
        return self._etsi(luku) is not None

    def lisaa(self, lisättävä):
        if not self.kuuluu(lisättävä):
            if self.koko == len(self.taulukko):
                self._kasvata_jonoa()

            self.taulukko[self.koko] = lisättävä
            self.koko += 1

            return True
        else:
            return False

    def poista(self, poistettava):
        n_indeksi = self._etsi(poistettava)

        if n_indeksi is not None:
            self.koko -= 1
            for j in range(n_indeksi, self.koko):
                self.taulukko[j] = self.taulukko[j + 1]
            self.taulukko[self.koko] = 0
            return True
        else:
            return False

    def mahtavuus(self):
        return self.koko

    def to_int_list(self):
        return list(self._iteroi_sisalto())

    @staticmethod
    def yhdiste(a, b):
        tulos = IntJoukko()

        for luku in a._iteroi_sisalto():
            tulos.lisaa(luku)

        for luku in b._iteroi_sisalto():
            tulos.lisaa(luku)

        return tulos

    @staticmethod
    def leikkaus(a, b):
        tulos = IntJoukko()

        for luku in a._iteroi_sisalto():
            if b.kuuluu(luku):
                tulos.lisaa(luku)

        return tulos

    @staticmethod
    def erotus(a, b):
        tulos = IntJoukko()

        for luku in a._iteroi_sisalto():
            tulos.lisaa(luku)

        for luku in b._iteroi_sisalto():
            tulos.poista(luku)

        return tulos

    def __str__(self):
        sisempi_teksti = ", ".join(map(str, self._iteroi_sisalto()))
        return f"{{{sisempi_teksti}}}"
