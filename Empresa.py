estoque = []
cadastro = []
desc = []
stop = 0 

while True:
        print('Digite a opção que deseja!')
        funcao = input('Cadastrar - Adicionar - Retirar - Visualizar\n')

        if funcao == 'Cadastrar' or funcao == 'cadastrar':
                nome = input('Digite qual o produto que deseja cadastrar, e \'0\' para parar: ')
                while nome !='0':
                        dec = input('Escreva e descrição:\n')
                        cadastro.append(nome)
                        desc.append(dec)
                        nome = input('Digite qual o produto que deseja cadastrar, e \'0\' para parar: ')
        elif funcao == 'Adicionar' or funcao == 'adicionar':
                escolha = input('Deseja ver o código de algum produto?\n')
                if escolha=='sim' or escolha=='Sim':
                        qual = input('Digite o produto cadastrado que deseja saber o código:\n')
                        print(cadastro.index(qual))
                add = int(input('Digite o código do produto:\n'))
                qnt = int(input('Digite a quantidade de produto:\n'))
                while stop <qnt:
                        estoque.append(cadastro[add]) 
                        stop += 1
                stop=0        
        elif funcao == 'Retirar' or funcao == 'retirar':
                escolha = input('Deseja ver os produtos em estoque?\n')
                if escolha=='sim' or escolha=='Sim':
                        print(estoque)
                add = input('Digite produto que deseja remover:\n')
                qnt = int(input('Digite a quantidade de produto a ser removido:\n'))
                while stop <qnt:
                        estoque.remove(add)
                        stop += 1
        elif funcao == 'Visualizar' or funcao == 'visualizar':
                for i in range (len(estoque)):
                        print(estoque[i])
                qual = input('Digite o produto cadastrado que deseja saber o código:\n')
                print(cadastro.index(qual))
                curi = int(input('Digite o código do item que deseja saber quantidade e descrição:\n'))
                if qual in cadastro and qual not in estoque:
                        print(qual,' não encontrasse em estoque')
                        print('Necessário nova encomenda')
                        print(desc[curi])
                elif estoque.count(qual) >0 and estoque.count(qual)<=50:
                        print(f'Há {estoque.count(qual)} unidades de {qual}')
                        print('Não está em falta, e nem necessário novo pedido!')
                        print(desc[curi])
                else:
                        print(f'Há {estoque.count(qual)} unidades de {qual}')
                        print(f'Estoque para {qual} se encontra cheio, não é necessário nova encomenda')
                        print(desc[curi])