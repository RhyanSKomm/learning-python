# Escreva um algoritmo que leia um valor inicial A e imprima a sequência de valores do cálculo do
# Fatorial: A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120

num=int(input("Digite um número: "))
i=num-1
fatorial=num
x=num

while i>0:
    
    fatorial=fatorial*i
    i-=1
    print(fatorial)

print(f"!{num} =",end=" ")
while x>0:
    if x==1:
        print(f"{x} = {fatorial}")
    else:
        print(f"{x} x ",end="")

    x-=1