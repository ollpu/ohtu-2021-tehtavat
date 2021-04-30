# "Muistava tekoäly"
class TekoalyParannettu:
    def __init__(self, muistin_koko=10):
        self._muisti = []
        self._muistin_koko = muistin_koko

    def anna_siirto(self):
        if len(self._muisti) <= 1:
            return "k"

        viimeisin_siirto = self._muisti[-1]

        maara = {"k": 0, "p": 0, "s": 0}

        for i in range(len(self._muisti) - 1):
            if viimeisin_siirto == self._muisti[i]:
                seuraava = self._muisti[i + 1]
                maara[seuraava] += 1

        # Tehdään siirron valinta esimerkiksi seuraavasti;
        # - jos kiviä eniten, annetaan aina paperi
        # - jos papereita eniten, annetaan aina sakset
        # muulloin annetaan aina kivi
        k, p, s = (maara["k"], maara["p"], maara["s"])
        if k > p or k > s:
            return "p"
        elif p > k or p > s:
            return "s"
        else:
            return "k"

        # Tehokkaampiakin tapoja löytyy, mutta niistä lisää
        # Johdatus Tekoälyyn kurssilla!

    def aseta_siirto(self, siirto):
        if len(self._muisti) == self._muistin_koko:
            self._muisti.pop(0)
        self._muisti.append(siirto)
