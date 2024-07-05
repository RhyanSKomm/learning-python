M=[[1,2,3],[4,5,6],[7,8,9]]
lista=[[],[],[]]

for i in M:
    lista[0].append(i[0])
    lista[1].append(i[1])
    lista[2].append(i[2])
print(lista)