matriz=[[1,120,-3],[4,5,250],[7,0,9]]
maior, linhaM, colunaM, menor, linham, colunam = -999,0,0,999,0,0
for i in range(len(matriz)):
    for j in range(len(matriz)):
         if matriz[i][j] > maior:
            linhaM = i
            colunaM = j
            maior = matriz[i][j]
for e in range(len(matriz)):
    for r in range(len(matriz)):
         if matriz[e][r] < menor:
            linham = e
            colunam = r
            menor = matriz[e][r]
print(maior,linhaM,colunaM)
print(menor,linham,colunam)