# Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas.
# Imprima as consoantes.

lista=[]
consoantes=[]
i=0
quant=0

while i<10:
    print(f"({1+i}) - ",end="")
    lista.append(str(input("Digite uma letra: ")))
    i+=1

for letra in lista:
    if letra=="a" or letra=="e" or letra=="i" or letra=="o" or letra=="u" or letra=="A" or letra=="E" or letra=="I" or letra=="O" or letra=="U":
        continue
    else:
        quant+=1
        consoantes.append(letra)

print(f"Consoantes lidas: {quant}\nConsoantes: {consoantes}")