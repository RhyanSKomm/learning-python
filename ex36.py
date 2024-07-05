# Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a
# média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

x=0
media=[]

aprovados=0

while x<10:
    print(f"Aluno {x+1}: ")
    y=0
    soma=0
    while y<4:
        nota=float(input("Digite uma nota: "))
        if nota not in range(0,11):
            print("Nota inválida")
            continue
        soma+=nota
        y+=1
    media.append(soma/4)
    print(media[x])
    x+=1

for medias in media:
    if medias>=7:
        aprovados+=1
print(f"Número de alunos aprovados: {aprovados}")
print("Alunos aprovados:")
for medias in media:
    if medias>=7:
        print(f"Aluno {media.index(medias)}: {medias}")