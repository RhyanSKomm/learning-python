def pescador(peso):
    maximo = 50
    mult = 4
    
    global excesso

    excesso = peso-maximo
    
    multa = excesso*mult

    return multa

pes = int(input('Digite o peso: '))

print('Valor a ser de taxa a ser pago:', pescador(pes))
print(f'Valor excedido: {excesso}')





