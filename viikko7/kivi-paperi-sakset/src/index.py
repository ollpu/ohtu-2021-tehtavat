from pelimuodot import kaksinpeli, yksinpeli_tekoaly, yksinpeli_parannettu_tekoaly

def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()

        if vastaus == "a":
            peli = kaksinpeli()
        elif vastaus == "b":
            peli = yksinpeli_tekoaly()
        elif vastaus == "c":
            peli = yksinpeli_parannettu_tekoaly()
        else:
            break

        peli.pelaa()


if __name__ == "__main__":
    main()
