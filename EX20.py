lista=[]
n2=1
n3=n2
while n2 !=0:
    n2=int(input("Digite o numero que deseja adicionar a lista e se 0 for adicionado a lista o programa para "))
    lista.append(n2)
print(lista)
if n2 %2==1:
    print("Esse numero e impar ",n2)