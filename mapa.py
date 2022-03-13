import random
import numpy as np


# generacja mapy 100 na 100
def map_gener():
    mapa = np.zeros((100, 100))
    # generacja n punktów dostawy
    n = random.randint(400, 600)
    for i in range(n-1):
        a = random.randint(0, 9999)
        b = int(a/100)
        c = a % 100
        mapa[b][c] = 1
    # generacja magazynu
    a = random.randint(0, 9999)
    b = int(a/100)
    c = a % 100
    mapa[b][c] = 2
    return mapa


# koordynaty magazynu
def magazyn_kord(mapa):
    result = np.where(mapa == 2)
    magazyn = [int(result[0]), int(result[1])]
    return magazyn


# koordynaty dostaw
def dostawa_kord(mapa):
    result = np.where(mapa == 1)
    dostawa = []
    for i in range(len(result[0])):
        dostawa.append([int(result[0][i]), int(result[1][i])])
    return dostawa
