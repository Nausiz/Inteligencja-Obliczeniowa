# przykładowa generacja miejsc na mapie
from mapa import map_gener, magazyn_kord, dostawa_kord
import matplotlib.pyplot as plt
import pandas as pd

mapa = map_gener()
magazyn = magazyn_kord(mapa)
dostawa = dostawa_kord(mapa)
# print(mapa)
print(f'Magazyny: {magazyn}')
print(f'Dostawy: {dostawa}')

mg = pd.DataFrame(magazyn, columns=['x', 'y'])
dst = pd.DataFrame(dostawa, columns=['x', 'y'])
# print(mg)
plt.plot(mg['x'], mg['y'], '.g')
plt.plot(dst['x'], dst['y'], '.y')
plt.show()
