#print("Test")
#print("Test2")
#print("Test3")
#print("Test4")

#przykładowa generacja miejsc na mapie
import random
import numpy as np

mapa = np.zeros((100, 100))
n = random.randint(400, 600)
for i in range(n):
    a = random.randint(0, 9999)
    b = int(a/100)
    c = a % 100
    mapa[b][c] = 1
print(mapa)
