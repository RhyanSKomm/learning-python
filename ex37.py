# Escreva um programa que receba um número inteiro maior do que 1, e verifique se o número
# fornecido é primo ou não.

num=int(input("Digite um número: "))
menor=0
i=20

while not i==1:
    if (num%i)==0:
        menor=i
        i-=1
    else:
        i-=1
        continue

if menor==0 or num==menor:
    print("Número primo")
else:
    print(f"Número não é primo")