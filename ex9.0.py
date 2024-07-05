def calcularTempo(tempo_minutos):
    
    horas = tempo_minutos / 60

    valor_minimo = 9.00

    
    valor_adicional = 1.50

    if horas <= 0.25:  
        return 0.00
    else:
        valor_total = valor_minimo + (horas - 1) * valor_adicional
        return round(valor_total, 2)


tempo_utilizado = int(input('Digite os minutos:'))
 
valor_a_pagar = calcularTempo(tempo_utilizado)
print(f"O valor a pagar é R${valor_a_pagar:.2f}")
