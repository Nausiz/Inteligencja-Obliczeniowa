class Samochod:

    def __init__(self, zaladunek_czas, pozycja, pojemnosc, predkosc, aktualny_zaladunek, kurs_wykonany, kolor):
        self.rozladunek_czas = 2
        self.zaladunek_czas = zaladunek_czas
        self.pozycja = pozycja
        self.pojemnosc = pojemnosc
        self.predkosc = predkosc
        self.aktualny_zaladunek = aktualny_zaladunek
        self.kurs_wykonany = kurs_wykonany
        self.kolor = kolor


    # magazyn jako indeks 0-4
    @property
    def pozycja(self):
        return self._pozycja

    @pozycja.setter
    def pozycja(self, value):
        self._pozycja = value

    # czy wykonał przynajmniej jeden kurs
    @property
    def kurs_wykonany(self):
        return self._kurs_wykonany

    @kurs_wykonany.setter
    def kurs_wykonany(self, value: bool):
        self._kurs_wykonany = value


    @property
    def aktualny_zaladunek(self):
        return self._aktualny_zaladunek

    @aktualny_zaladunek.setter
    def aktualny_zaladunek(self, value):
        self._aktualny_zaladunek = value

    def __str__(self):
        return f'Kolor: {self.kolor}, '\
               f'Pojemnosc: {self.pojemnosc}, '\
               f'Predkosc: {self.predkosc}, ' \
               f'Zaladunek: {self.zaladunek_czas}, ' \
               f'Rozladunek: {self.rozladunek_czas}, '\
               f'Aktualny zaladunek: {self.aktualny_zaladunek}, '\
               f'Pozycja: {self.pozycja}, ' \
               f'Kurs wykonany: {self.kurs_wykonany}'

pass
