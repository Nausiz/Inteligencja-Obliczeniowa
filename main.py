# przykładowa generacja miejsc na mapie
from mapa import map_gener, magazyn_kord, dostawa_kord
from samochody import losuj_samochody
from Klasy.utils import najblizszy_punkt, najblizszy_magazyn, czas, sprawdz_przerwe
import plotly.express as px
import pandas as pd
import random


mapa = map_gener()
magazyn = magazyn_kord(mapa)
dostawa = dostawa_kord(mapa)
samochody = losuj_samochody(magazyn)

liczba_punktów = len(dostawa) + len(magazyn)

# print(mapa)
print(f'Magazyny: {magazyn}')
print(f'Dostawy: {dostawa}')

print(*samochody, sep='\n')

mg = pd.DataFrame(magazyn, columns=['x', 'y'])
dst = pd.DataFrame(dostawa, columns=['x', 'y', 'wielkosc', 'dostarcz/odbierz'])
print(dst)

#print(najblizszy_punkt(samochody[0], dostawa))

fig = px.scatter(dst, x='x', y='y', color=dst['dostarcz/odbierz'])
fig.add_scatter(x=mg['x'], y=mg['y'], mode="markers", name='magazyn')
fig.show()

# d = {'x': [0, 1, 2, 3], 'y': [0, 1, 2, 3]}
# df1 = pd.DataFrame(data=d)
# d = {'x': [32, 12, 11, 13], 'y': [0, 1, 2, 3]}
# df2 = pd.DataFrame(data=d)

# tab = [df1, df2]
trasy = []
for s in samochody:
    trasy.append({'x': [s.pozycja[0]], 'y': [s.pozycja[1]]})
# trasa = {'x': [], 'y': []}

uni = (random.choice(dostawa))
while True:
    for i, s in enumerate(samochody):
        p = najblizszy_punkt(s, dostawa)
        dostarczony = [j for j, x in enumerate(dostawa) if x[0] == p[0] and x[1] == p[1]]

        if len(dostarczony) > 0:

            if dostawa[dostarczony[0]][3] == 'Odbierz':
                # Załaduj samochód
                s.aktualny_zaladunek = s.aktualny_zaladunek + dostawa[dostarczony[0]][2]

            else:
                # Rozładuj samochód
                s.aktualny_zaladunek = s.aktualny_zaladunek - dostawa[dostarczony[0]][2]

            # Zaktualizuj łączny czas, licznik do przerwy i przebytą odległość
            s.czas_do_przerwy += czas(s, p[2])
            s.czas += czas(s, p[2]) + (s.zaladunek_czas * dostawa[dostarczony[0]][2])
            s.przebyta_droga += p[2]

            # Sprawdź czy przerwa | nowe zalecenie kierownika
            sprawdz_przerwe(s)

            #print(round(s.czas, 2), ", ", round(s.czas_do_przerwy, 2))

            # Sprawdź czy punkt odpoczynku ze studentami | nowe zalecenie kierownika
            if dostawa[dostarczony[0]] == uni:
                s.czas += 720 # dwunastogodzinna przerwa

            dostawa.pop(dostarczony[0])

        else:
            p = najblizszy_magazyn(s, magazyn)
            s.aktualny_zaladunek = s.pojemnosc * 0.8

        trasy[i]['x'].append(p[0])
        trasy[i]['y'].append(p[1])
        if len(dostawa) == 0:
            break
    if len(dostawa) == 0:
        break

tab = []
for i in range(len(samochody)):
    df = pd.DataFrame(data=trasy[i])
    tab.append(df)
#print(trasa)
for i, t in enumerate(tab):
    fig.add_scatter(x=t['x'], y=t['y'], name=f'samochod_{i+1}')

czas_fin = []
dlugosc_fin = []
for s in samochody:
    czas_fin.append(round(s.czas/60,2))
    dlugosc_fin.append(round(s.przebyta_droga,2))

print("Liczba punktów na mapie (z magazynami): ", liczba_punktów)
print("Liczba samochodów: ", len(samochody))
print("Czasy przejazdu samochodów (w godzinach): ", czas_fin, "\nPokonana odległość (w kilometrach): ", dlugosc_fin)
fig.show()
