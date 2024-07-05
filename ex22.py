# Escreva um programa que permita a qualquer aluno introduzir, pelo teclado, uma sequência de
# notas (válidas no intervalo de 0 a 10) e que mostre na tela, como resultado, a correspondente
# média aritmética. O número de notas com que o aluno pretenda efetuar o cálculo não
# fornecido ao programa, o qual terminará quando for introduzido um valor que não seja válido
# como nota de aprovação.

infinito=True
notas=[]
nota=0
while infinito==True:
    nota=float(input("Digite uma nota: "))
    if nota in range(0,11):
        notas.append(nota)
    elif nota not in range(0,11):
        print("Nota inválida, encerrando cálculo.")
        break

media=sum(notas)/len(notas)
print(f"\nQuantidade de notas: {len(notas)}")
print(f"Média: {media}")