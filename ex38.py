# Escreva um programa que leia um inteiro não negativo n e imprima a soma dos n primeiros
# números primos

cont=int(input("\nDigite um número: "))
primos=[]
fin=0
num=2

if cont>0:
    while fin<cont:
        for x in range(2,num+1):
            if num%x==0:
                if x==num:
                    primos.append(num)
                    fin+=1
                    num+=1
                elif x!=num:
                    num+=1
                    continue
            else:

                continue

    soma=sum(primos)
    if cont==1:
        print(f"\nPrimeiro número primo: {primos}")
        print(f"A soma do primeiro número primo é: {soma}\n")
        
    else:
        print(f"\n{cont} primeiros números primos: {primos}")
        print(f"A soma dos {cont} primeiros números primos é: {soma}\n")

else:
    print("\nValor inválido\n")