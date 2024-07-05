# Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse
# número, com exceção dele próprio. Ex: a soma dos divisores do número 66 é:
# 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78

divisores=[]
num=int(input("Digite um número: "))

for i in range(1,num):
    if num%i==0:
        divisores.append(i)
    else:
        continue

print(f"A soma dos divisores do número {num} é:")
for num in divisores:
    if num==divisores[-1]:
        print(num,"=",sum(divisores))
        break
    print(num,"+", end=" ")