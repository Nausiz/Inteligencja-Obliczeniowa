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

        if kolor == "Zielony":
            zaladunek_czas = 1
            predkosc = 1.5
            pojemnosc = 1000

        elif kolor == "Niebieski":
            zaladunek_czas = 2
            predkosc = 1
            pojemnosc = 1500

        elif kolor == "Czerwony":
            zaladunek_czas = 3
            predkosc = 0.75
            pojemnosc = 2000

        s = Samochod(zaladunek_czas, pozycja, pojemnosc, predkosc, kurs_wykonany, kolor)

        # print(s)
        samochody.append(s)
    return samochody
