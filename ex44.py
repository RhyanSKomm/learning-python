# Crie um programa que apresente um menu de opções para o cálculo das seguintes operações
# entre dois números.

# • adição (opção 1)
# • subtração (opção 2)
# • multiplicação (opção 3)
# • divisão (opção 4).
# • saída (opção 5)

# O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do
# resultado e a volta ao menu de opções. O programa só termina quando for escolhida a opção
# de saída (opção 5).

infinito=True

while infinito==True:
    print("\n• Adição (opção 1)\n• Subtração (opção 2)\n• Multiplicação (opção 3)\n• Divisão (opção 4)\n• Saída (opção 5)")
    op1=int(input())

    if op1==1:
        x=float(input("\nDigte o valor de X: "))
        y=float(input("Digte o valor de Y: "))

        print(f"\nA soma dos números é: {x+y}")

    elif op1==2:
        x=float(input("\nDigte o valor de X: "))
        y=float(input("Digte o valor de Y: "))

        print(f"\nA subtração entre os números é: {x-y}")

    elif op1==3:
        x=float(input("\nDigte o valor de X: "))
        y=float(input("Digte o valor de Y: "))

        print(f"\nO produto dos números é: {x*y}")

    elif op1==4:
        x=float(input("\nDigte o valor de X: "))
        y=float(input("Digte o valor de Y: "))

        print(f"\nA divisão entre os números é: {x/y}")

    elif op1==5:
        print("\nSaindo...\n")
        break

    else:
        print("\nOpção inválida")