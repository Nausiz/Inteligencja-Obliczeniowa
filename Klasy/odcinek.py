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
    # km
    def odleglosc(self) -> float:
        return round(((self._punktB[0]-self._punktA[0])**2+(self._punktB[1]-self._punktA[1])**2)**(1/2), 2)

    # minuty
    def czas(self) -> float:
        return round(self.odleglosc()/self._samochod._predkosc, 2)



