import math
from samochody import Samochod

def najblizszy_punkt(samochod: Samochod, lista_punktow: list) -> list:
    min_dlugosc = math.sqrt((lista_punktow[0][0]-samochod.pozycja[0])**2+(lista_punktow[0][1]-samochod.pozycja[1])**2)
    min_x = 0
    min_y = 0
    for row in lista_punktow:
        dlugosc = math.sqrt((row[0]-samochod.pozycja[0])**2+(row[1]-samochod.pozycja[1])**2)
        if dlugosc < min_dlugosc:
            min_dlugosc = dlugosc
            min_x = row[0]
            min_y = row[1]

    return [min_x, min_y]
