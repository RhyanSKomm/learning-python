# Faça um programa que conte quantos números primos existem entre a e b, onde a e b são
# números informados pelo usuário.

primos=[]
a=int(input("\nDigite o início do intervalo: "))
b=int(input("Digite o fim do intervalo: "))
num=a

for num in range(a,b+1):
    for x in range(2,num+1):
        if num%x==0:
            if x==num:
                primos.append(num)
                num+=1

            elif x!=num:
                num+=1
                continue

        else:
            continue

print(f"\nNúmeros primos entre {a} e {b}: {primos}")
print(f"Quantidade de números primos: {len(primos)}\n")
