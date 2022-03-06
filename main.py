# print("Test")
# print("Test2")
# print("Test3")
# print("Test4")

# przykładowa generacja miejsc na mapie
import random
import numpy as np

# generacja mapy 100 na 100
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
print(mapa)

#koordynaty magazynu
result = np.where(mapa == 2)
magazyn = [int(result[0]), int(result[1])]
print(magazyn)
