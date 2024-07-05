# Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e
# escreva para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize a entrada
# de dados com um valor negativo ou zero.

lista=[]
infinito=True

while infinito==True:
    num=int(input("Digite um valor: "))

    if num<=0:
        break
    
    lista.append(num)

print("\nFinalizando entrada\n\nValores: ")
for i in lista:
    quad=i**2
    cubo=i**3
    raiz=i**0.5
    print(f"Número: {i}   Quadrado: {quad}    Cubo: {cubo}    Raiz: {raiz:.2f}")
print("")