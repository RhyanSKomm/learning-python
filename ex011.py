matriz=[[1,2,11,13],[4,15,16,60],[7,8,19,200],[20,100,5,3]]
maior, linha, coluna = 0,0,0
for i in range(len(matriz)):
    for j in range(len(matriz)):
         if matriz[i][j] > maior:
            linha = i
            coluna = j
            maior = matriz[i][j]
print(maior,linha,coluna)