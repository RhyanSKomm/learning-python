# Faça um programa que gera um número aleatório de 1 a 100. O usuário deve tentar acertar
# qual o número foi gerado, a cada tentativa o programa deverá informar se o chute e menor ou
# maior que o número gerado. O programa acaba quando o usuário acerta o número gerado. O
# programa deve informar em quantas tentativas o número foi descoberto.

import random

infinito=True
tentativas=0
num=random.randint(1,100)

while infinito==True:

    tentativas+=1

    chute=int(input("\nTente adivinhar o número: "))

    if chute!=num:
        if chute<num:
            print("Chute é menor do que o número")
        elif chute>num:
            print("Chute é maior do que o número")
    else:
        break

print("\nAcertou!")
print(f"Quantidade de tentativas: {tentativas}")