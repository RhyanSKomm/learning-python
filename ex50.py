# Dados n e dois números inteiros positivos, i e j, diferentes de 0, imprimir em ordem crescente
# os n primeiros naturais que são múltiplos de i ou de j e ou de ambos. Exemplo: Para n = 6, i = 2
# e j = 3 a saída deverá ser: 0,2,3,4,6,8.

lista=[]
n=int(input("Digite a duração do processo: "))
i=int(input("Digite um número: "))
j=int(input("Digite outro número: "))
x=0

while len(lista)!=n:
    if x%i==0:
        lista.append(x)
    elif x%j==0:
        lista.append(x)
    x+=1

print(lista)
