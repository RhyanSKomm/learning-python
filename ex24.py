# Crie um programa que some todos os números naturais abaixo de 1000 que são múltiplos de 3
# ou 5.

multiplos=[]
for num in range (0,1001):
    if num%3==0 or num%5==0:
        multiplos.append(num)

print(f"Soma: {sum(multiplos)}")