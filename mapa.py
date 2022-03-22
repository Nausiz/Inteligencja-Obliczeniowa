import random


# generacja mapy 100 na 100
def map_gener():
    mapa = []
    for i in range(10000):
        b = int(i / 100)
        c = i % 100
        mapa.append([b, c, ""])
    # generacja n punktów dostawy
    n = random.randint(405, 605)
    # print(f'n:{n}')
    points = random.sample(range(10000), n)
    for i in range(n-5):
        a = points[i]
        mapa[a][2] = "dostawa"
    # generacja magazynu
    for i in range(5):
        a = points[n-5+i]
        mapa[a][2] = "magazyn"
    return mapa


# koordynaty magazynu
def magazyn_kord(mapa):
    result = [i for i, x in enumerate(mapa) if x[2] == "magazyn"]
    magazyn = []
    for i in range(5):
        magazyn.append([mapa[int(result[i])][0], mapa[int(result[i])][1]])
    return magazyn


# koordynaty dostaw i wielkość towaru
def dostawa_kord(mapa):
    result = [i for i, x in enumerate(mapa) if x[2] == "dostawa"]
    dostawa = []
    for i in range(len(result)):
        dostawa.append([mapa[int(result[i])][0], mapa[int(result[i])][1],
                        random.randint(100, 200), random.choice(["Dostarcz", "Odbierz"])])
    return dostawa
