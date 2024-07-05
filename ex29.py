# Crie um programa que calcule o menor número divisível por cada um dos números de 1 a 20?
# Ex: 2520 e o menor número que pode ser dividido por cada um dos números de 1 a 10, sem
# sobrar resto.

num=(int(input("Digite um número: ")))
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
    print("Número primo, somente divisível por 1 e ele mesmo.")
else:
    print(f"Menor número divisível: {menor}")