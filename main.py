# przykładowa generacja miejsc na mapie
from mapa import map_gener, magazyn_kord, dostawa_kord
from samochody import losuj_samochody, Samochod
from Klasy.utils import najblizszy_punkt
import matplotlib.pyplot as plt
import pandas as pd


mapa = map_gener()
magazyn = magazyn_kord(mapa)
dostawa = dostawa_kord(mapa)
samochody = losuj_samochody(magazyn)

# print(mapa)
print(f'Magazyny: {magazyn}')
print(f'Dostawy: {dostawa}')

print(*samochody, sep='\n')

mg = pd.DataFrame(magazyn, columns=['x', 'y'])
dst = pd.DataFrame(dostawa, columns=['x', 'y', 'wielkosc', 'dostarcz/odbierz'])
print(dst)
plt.plot(mg['x'], mg['y'], '.g')
plt.plot(dst['x'], dst['y'], '.y')
plt.show()

print(najblizszy_punkt(samochody[0], dostawa))
