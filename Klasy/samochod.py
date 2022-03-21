class Samochod:
    # rozładunek w sekundach
    rozladunek_czas = 2

    # załadunek w sekundach/kg
    @property
    def zaladunek_czas(self):
        return self._zaladunek_czas

    @zaladunek_czas.setter
    def zaladunek_czas(self, value: float):
        self._zaladunek_czas = value

    # pojemność w kg
    @property
    def pojemnosc(self):
        return self._pojemnosc

    @pojemnosc.setter
    def pojemnosc(self, value: int):
        self._pojemnosc = value

    # prędkość w km/min
    @property
    def predkosc(self):
        return self._predkosc

    @predkosc.setter
    def predkosc(self, value: float):
        self._predkosc = value

    # magazyn jako indeks 0-4
    @property
    def magazyn(self):
        return self._magazyn

    @magazyn.setter
    def magazyn(self, value: int):
        self._magazyn = value

    # czy wykonał przynajmniej jeden kurs
    @property
    def kurs_wykonany(self):
        return self._kurs_wykonany

    @kurs_wykonany.setter
    def kurs_wykonany(self, value: bool):
        self._kurs_wykonany = value

    @property
    def kolor(self):
        return self._kolor

    @kolor.setter
    def kolor(self, value: str):
        self._kolor = value

    def __str__(self):
        return f'Kolor: {self.kolor}, '\
               f'Pojemnosc: {self.pojemnosc}, '\
               f'Predkosc: {self.predkosc}, ' \
               f'Zaladunek: {self.zaladunek_czas}, ' \
               f'Rozladunek: {self.rozladunek_czas}, ' \
               f'Magazyn: {self.magazyn}, ' \
               f'Kurs wykonany: {self.kurs_wykonany}'


pass


