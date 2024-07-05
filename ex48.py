# Dada uma sequência de 3 números inteiros, determinar o número de vezes que cada um deles
# ocorre em uma lista. Comparar se os digitados aparecem na lista. Para exemplificar, considere:

# Lista: [1, 1, 4, 5, 6, 7, 3, 2, 2, -1]
# Entrada: 1, 2 e 3
# Saída:
# 1: ocorreu 2 vezes
# 2: ocorreu 2 vezes
# 3: ocorreu 1 vez

lista= [1, 1, 4, 5, 6, 7, 3, 2, 2, -1]

num1=int(input("Digite um número: "))
num2=int(input("Digite outro número: "))
num3=int(input("Digite mais um número: "))
found1=0
found2=0
found3=0

for item in lista:
    if item==num1:
        found1+=1
    elif item==num2:
        found2+=1
    elif item==num3:
        found3+=1

print(f"{num1}: Ocorreu {found1} vezes")
print(f"{num2}: Ocorreu {found2} vezes")
print(f"{num3}: Ocorreu {found3} vezes")