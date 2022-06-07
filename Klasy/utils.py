import math
from samochody import Samochod


def najblizszy_punkt(samochod: Samochod, lista_punktow: list) -> list:
    min_dlugosc = 200
    min_x = -1
    min_y = -1
    for row in lista_punktow:
        dlugosc = math.sqrt((row[0]-samochod.pozycja[0])**2+(row[1]-samochod.pozycja[1])**2)
        if dlugosc < min_dlugosc:
            czy_odbior = (row[3] == 'Odbierz')
            if czy_odbior:
                zaladunek_po_odbiorze = row[2] + samochod.aktualny_zaladunek
            else:
                zaladunek_po_odbiorze = samochod.aktualny_zaladunek - row[2]
            if czy_odbior and zaladunek_po_odbiorze <= samochod.pojemnosc:
                min_dlugosc = dlugosc
                min_x = row[0]
                min_y = row[1]
            elif not czy_odbior and zaladunek_po_odbiorze > 0:
                min_dlugosc = dlugosc
                min_x = row[0]
                min_y = row[1]
    if min_dlugosc < 200:
        samochod.pozycja = [min_x, min_y]
    return [min_x, min_y]


def najblizszy_magazyn(samochod: Samochod, lista_punktow: list) -> list:
    min_dlugosc = 200
    min_x = -1
    min_y = -1
    for row in lista_punktow:
        dlugosc = math.sqrt((row[0] - samochod.pozycja[0]) ** 2 + (row[1] - samochod.pozycja[1]) ** 2)
        if dlugosc < min_dlugosc:
            min_dlugosc = dlugosc
            min_x = row[0]
            min_y = row[1]
    samochod.pozycja = [min_x, min_y]
    return [min_x, min_y]
