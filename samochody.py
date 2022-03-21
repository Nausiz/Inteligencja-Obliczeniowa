from Klasy.samochod import Samochod
import random

def losuj_samochody():
    lb_samochodow = random.randint(3,6)
    samochody = []
    #print(lb_samochodow)

    for i in range (lb_samochodow):
        s = Samochod()
        s.kurs_wykonany = False
        s.kolor = random.choice(["Zielony", "Niebieski", "Czerwony"])
        s.magazyn = random.randint(0,4)

        if s.kolor == "Zielony":
            s.zaladunek_czas= 1
            s._predkosc = 1.5
            s.pojemnosc= 1000

        elif s.kolor == "Niebieski":
             s.zaladunek_czas = 2
             s._predkosc = 1
             s.pojemnosc = 1500

        elif s.kolor == "Czerwony":
            s.zaladunek_czas= 3
            s._predkosc = 0.75
            s.pojemnosc= 2000

        #print(s)
        samochody.append(s)
    return samochody

