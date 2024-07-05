# Elabore um programa que faça leitura de vários números inteiros, até que se digite um número
# negativo. O programa tem que retornar o maior e o menor número lido.

nums=[]
infinito=True
i=0

while infinito==True:
    num=int(input("Digite um número: "))
    if num<0:
        break
    else:
        nums.append(num)

print(f"Maior número: {max(nums)}")
print(f"Menor número: {min(nums)}")