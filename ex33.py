# Escreva um algoritmo que leia um vetor com 10 posições de números inteiros. Em seguida
# receba um novo valor do usuário e verifique se este valor se encontra no vetor.

vet=[]
i=0

while i<10:
    print(f"({1+i}) - ",end="")
    vet.append(int(input("Digite um número: ")))
    i+=1

search=int(input("Digite um número para buscar: "))

for item in vet:
    if item==search:
        print(f"\nValor encontrado!")
if search not in vet:
    print("Valor não encontrado")