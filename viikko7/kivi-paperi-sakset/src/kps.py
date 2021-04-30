from tuomari import Tuomari

class KPS:
    def pelaa(self):
        print(
            "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
        )

        tuomari = Tuomari()

        while True:
            ekan_siirto = self._kysy_ensimmaisen_siirto()
            tokan_siirto = self._kysy_toisen_siirto()
            self._ilmoita_ensimmaisen_siirto(ekan_siirto)

            if not self._siirto_ok(ekan_siirto) or not self._siirto_ok(tokan_siirto):
                break

            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

        print("Kiitos!")
        print(tuomari)

    def _kysy_ensimmaisen_siirto(self):
        raise NotImplementedError

    def _kysy_toisen_siirto(self):
        raise NotImplementedError

    def _ilmoita_ensimmaisen_siirto(self, siirto):
        pass

    @staticmethod
    def _siirto_ok(siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
