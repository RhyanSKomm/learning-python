alunos = [('João',8.0),('Maria',9.5),('Pedro',7.5), ('Ana',8.5)]
sup = 0
aluno = 0
for i in alunos:
    if i[1]>sup:
        sup = i[1]
        aluno = i
print(aluno[0])