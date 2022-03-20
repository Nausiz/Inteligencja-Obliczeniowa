import random


# wielkość towaru do dostarczenia lub odebrania
def wielkosc_towaru(dostawa):
    towary = []
    for i in range(len(dostawa)):
        towary.append([random.randint(100, 200), random.choice(["Dostarcz", "Odbierz"])])
    return towary
