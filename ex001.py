empresa = []

for i in range(4):
    dic = {}
    nome = input('Digite o nome da empresa: ')
    unidade = input('Digite a Unidade: ')
    Fone = int(input('Digite o fone: '))
    email = input('Digite o email: ')
    cidade = input('Digite a cidade: ')
    uf = input('Digite o UF: ')
    
    dic['Nome']= nome
    dic['Unidade']= unidade
    dic['Fone']= Fone
    dic['E-mail']= email
    dic['cidade']=cidade
    dic['UF']= uf

    empresa.append(dic)

for i in empresa:
    print(i)
 