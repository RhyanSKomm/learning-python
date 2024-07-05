# Crie um programa que calcula a associação em paralelo de dois resistores R1 e R2 fornecidos
# pelo usuário via teclado. O programa fica pedindo estes valores e calculando até que o usuário
# entre com um valor para resistência igual a zero.

#      R1 * R2
#  R = -------
#      R1 + R2

infinito=True
while infinito==True:
    r1=float(input("\nDigite o valor de R1: "))
    if r1==0:
        break
    r2=float(input("Digite o valor de R2: "))
    if r2==0:
        break

    r=(r1*r2)/(r1+r2)
    print(f"\nResistência equivalente: {r}")

print('\n"0" digitado, encerrando programa...\n')