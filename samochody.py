from Klasy.samochod import Samochod
import random


def losuj_samochody(magazyny: list):
    lb_samochodow = random.randint(3, 6)
    samochody = []
    # print(lb_samochodow)

    for i in range(lb_samochodow):
        kurs_wykonany = False
        kolor = random.choice(["Zielony", "Niebieski", "Czerwony"])
        pozycja = random.choice(magazyny)

        zaladunek_czas = 0
        predkosc = 1.5
        pojemnosc = 1000
        aktualny_zaladunek = 0

        if kolor == "Zielony":
            zaladunek_czas = 0.016 #1 sekunda w minutach
            predkosc = 1.5
            pojemnosc = 1000
            aktualny_zaladunek = pojemnosc/2

        elif kolor == "Niebieski":
            zaladunek_czas = 0.033 #2 sekundy w minutach
            predkosc = 1
            pojemnosc = 1500
            aktualny_zaladunek = pojemnosc/2

        elif kolor == "Czerwony":
            zaladunek_czas = 0.05 #3 sekundy w minutach
            predkosc = 0.75
            pojemnosc = 2000
            aktualny_zaladunek = pojemnosc/2

        s = Samochod(zaladunek_czas, pozycja, pojemnosc, predkosc, aktualny_zaladunek, kurs_wykonany, kolor)

        # print(s)
        samochody.append(s)
    return samochody
