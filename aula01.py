### Uma super variável que contém index como chave e value

pessoa = {'nome':'Rhyan','idade': 18,'cidade':'CG'}

#PRINT NO TIPO
print(type(pessoa))

print('\n')

#PRINT NAS CHAVES E SEUS VALORES
print(pessoa.keys())
print(pessoa.values())

print('\n')

#PRINT NOS VALORES DE CHAVES ESPECIFÍCAS
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['cidade'])

print('\n')

#FOR NAS CHAVES
for i in pessoa.keys():
    print(i)

print('\n')

#FOR NOS VALORES
for i in pessoa.values():
    print(i)

print('\n')

#FOR NOS VALORES DE CHAVES ESPECÍFICAS
for i in pessoa.keys():
    print(pessoa[i])

print('\n')

#MUDANÇA NOS VALORES DE UMA CHAVE
pessoa['cidade'] = 'New York'
pessoa['idade'] = 22
