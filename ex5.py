def somaImposto(taxaImposto, custo):
    t = taxaImposto/100
    c =  custo+(custo*t)
    return c
imp = int(input('Digite o valor de imposto:'))
c = int(input('Digite o custo: '))

print(somaImposto(imp,c))