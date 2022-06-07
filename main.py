# przykładowa generacja miejsc na mapie
from mapa import map_gener, magazyn_kord, dostawa_kord
from samochody import losuj_samochody
from Klasy.utils import najblizszy_punkt, najblizszy_magazyn
import plotly.express as px
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

#print(najblizszy_punkt(samochody[0], dostawa))

fig = px.scatter(dst, x='x', y='y', color=dst['dostarcz/odbierz'])
fig.add_scatter(x=mg['x'], y=mg['y'], mode="markers", name='magazyn')

# d = {'x': [0, 1, 2, 3], 'y': [0, 1, 2, 3]}
# df1 = pd.DataFrame(data=d)
# d = {'x': [32, 12, 11, 13], 'y': [0, 1, 2, 3]}
# df2 = pd.DataFrame(data=d)

# tab = [df1, df2]
trasy = []
for s in samochody:
    trasy.append({'x': [s.pozycja[0]], 'y': [s.pozycja[1]]})
# trasa = {'x': [], 'y': []}
ile = 0
while True:
    for i, s in enumerate(samochody):
        p = najblizszy_punkt(s, dostawa)
        dostarczony = [j for j, x in enumerate(dostawa) if x[0] == p[0] and x[1] == p[1]]
        if len(dostarczony) > 0:
            if dostawa[dostarczony[0]][3] == 'Odbierz':
                s.aktualny_zaladunek = s.aktualny_zaladunek + dostawa[dostarczony[0]][2]
            else:
                s.aktualny_zaladunek = s.aktualny_zaladunek - dostawa[dostarczony[0]][2]
        else:
            p = najblizszy_magazyn(s, magazyn)
            s.aktualny_zaladunek = s.pojemnosc * 0.8
        if s.aktualny_zaladunek < 0:
            print(f'zjebało się {s.aktualny_zaladunek}')
        dostawa.pop(dostarczony[0])
        trasy[i]['x'].append(p[0])
        trasy[i]['y'].append(p[1])
        if len(dostawa) == 0:
            break
    if len(dostawa) == 0:
        break
    ile +=1
tab = []
for i in range(len(samochody)):
    df = pd.DataFrame(data=trasy[i])
    tab.append(df)
#print(trasa)
for i, t in enumerate(tab):
    fig.add_scatter(x=t['x'], y=t['y'], name=f'samochod_{i+1}')

fig.show()
