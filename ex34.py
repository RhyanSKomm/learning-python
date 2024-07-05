# Faça um Programa que leia 20 números inteiros e armazene-os em uma LISTA. Armazene os
# números pares na lista PAR e os números IMPARES na lista ímpar. Imprima os três vetores.

lista=[]
impar=[]
par=[]
i=0

while i<20:
    print(f"({1+i}) - ",end="")
    lista.append(int(input("Digite um número: ")))
    i+=1

for num in lista:
    if num%2==0:
        par.append(num)
    else:
        impar.append(num)

print(f"\nLista: {lista}")
print(f"Números pares: {par}")
print(f"Números impares: {impar}")