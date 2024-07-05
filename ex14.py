import random
def fun(a):
    word = list(a.lower())
    random.shuffle(word)
    return ''.join(word)

pl = str(input('Digite Uma Palavra: '))

print(fun(pl))