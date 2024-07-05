# Faça um programa que leia vários números, calcule e mostre:
# (a) A soma dos números digitados
# (b) A quantidade de números digitados
# (c) A média dos números digitados
# (d) O maior número digitado
# (e) O menor número digitado
# (f) A média dos números pares
# Finalize a entrada de dados caso o usuário informe o valor 0.

lista=[]
pares=[]
infinito=True

while infinito==True:
    num=int(input("Digite um número: "))

    if num==0:
        break

    lista.append(num)

for num in lista:
    if num%2==0:
        pares.append(num)

print(f"\nSoma dos números digitados: {sum(lista)}")
print(f"Quantidade de números digitados: {len(lista)}")
print(f"Média dos números digitados: {sum(lista)/len(lista)}")
print(f"Maior número digitado: {max(lista)}")
print(f"Menor número digitado: {min(lista)}")
print(f"Média dos números pares: {sum(pares)/len(pares)}\n")