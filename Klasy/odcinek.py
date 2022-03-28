from Klasy.samochod import Samochod

class Odcinek:
    def __init__(self, punktA: list, punktB: list, samochod: Samochod):
        self._punktA = punktA
        self._punktB = punktB
        self._samochod = samochod

    def __str__(self):
        return f"Z punkt A: {self._punktA} do punktu B: {self._punktB}."

    @property
    def od(self) -> list:
        return self._punktA

    @property
    def do(self) -> list:
        return self._punktB

    @property
    def samochod(self) -> Samochod:
        return self._samochod

    def odleglosc(self) -> float:
        return ((self._punktB[0]-self._punktA[0])**2+(self._punktB[1]-self._punktA[1])**2)**(1/2)

    def czas(self) -> float:
        if self._samochod.kolor == 'Zielony':
            return self.odleglosc()/self._samochod._predkosc
        elif self._samochod.kolor == 'Niebieski':
            return self.odleglosc()/self._samochod._predkosc
        else:
            return self.odleglosc()/self._samochod._predkosc


