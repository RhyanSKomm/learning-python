def calcularTempo(tempo_minutos):
    
    horas = tempo_minutos / 60

    valor_minimo = 9.00

    valor_adicional = 1.50

    if horas <= 0.25:  
        return 0.00
    else:
        valor_total = valor_minimo + (horas - 1) * valor_adicional
   
    pis = round(0.0033 * valor_total,2)
    cofins = round(0.0020 * valor_total,2)
    icms = round(0.17 * valor_total,2)
    total = valor_total-(pis + cofins + icms)
    
    print('Pis ',pis)
    print('COFINS ',cofins)
    print('ICMS ',icms)
    print('IMPOSTOS ',total)
    print('A PAGAR ',valor_total)
    
tempo_utilizado = int(input('Digite os minutos:'))
 
valor_a_pagar = calcularTempo(tempo_utilizado)



