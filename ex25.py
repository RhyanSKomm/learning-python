# Crie um programa que leia um número indeterminado de idades de indivíduos (pare quando
# for informada a idade 0), e calcule a idade média desse grupo.

infinito=True
idades=[]

print("Digite 0 para encerrar calculo.")
while infinito==True:
    idade=float(input("Digite uma idade: "))
    if idade==0:
        print("Encerrando calculo.")
        break
    idades.append(idade)

media=sum(idades)/len(idades)
print(f"\nIdades: {idades}")
print(f"Média das idades: {media:.2f}")