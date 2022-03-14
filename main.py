# przykładowa generacja miejsc na mapie
from mapa import map_gener, magazyn_kord, dostawa_kord

mapa = map_gener()
magazyn = magazyn_kord(mapa)
dostawa = dostawa_kord(mapa)
print(mapa)
print(f'Magazyny: {magazyn}')
print(f'Dostawy: {dostawa}')
