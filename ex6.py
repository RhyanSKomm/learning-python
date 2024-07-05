def tabela(qnt):
    cont = 0
    for i in range(qnt):
        cont+= 1.99
    return cont

items = int(input('Digite a quantidade de items: '))

print('Deve ser pago',tabela(items))