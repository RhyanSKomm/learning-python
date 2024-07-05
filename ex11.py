def var(x,z):
    cont = 1
    for i in range(z):
        cont*=x
    return cont

print(var(4,3))