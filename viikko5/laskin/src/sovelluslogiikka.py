class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.tulospino = []

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo

class LaskinOperaatio:
    def __init__(self, sovelluslogiikka, lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.lue_syote = lue_syote

    def suorita(self):
        entinen_tulos = self.sovelluslogiikka.tulos
        self.sovelluslogiikka.tulospino.append(entinen_tulos)
        self.suorita_toteutus()

class Summa(LaskinOperaatio):
    def suorita_toteutus(self):
        self.sovelluslogiikka.plus(self.lue_syote())

class Erotus(LaskinOperaatio):
    def suorita_toteutus(self):
        self.sovelluslogiikka.miinus(self.lue_syote())

class Nollaus(LaskinOperaatio):
    def suorita_toteutus(self):
        self.sovelluslogiikka.nollaa()

class Kumoa(LaskinOperaatio):
    def suorita(self):
        if len(self.sovelluslogiikka.tulospino):
            entinen_arvo = self.sovelluslogiikka.tulospino.pop()
            self.sovelluslogiikka.aseta_arvo(entinen_arvo)

