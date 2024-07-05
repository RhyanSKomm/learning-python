import random
numeros = []
def sorte():
    for i in range(5):
        n1 = random.randint(0,100)
        numeros.append(n1)
def somaPar():
    return sum(numeros)

sorte()

print(numeros)

print(somaPar())