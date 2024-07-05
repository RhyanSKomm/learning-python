def financiamento(vv,ve,tj,qp):
    cv = (vv-ve) * (1+(tj/100))**qp
    return round(cv,2)
    
a = float(input('Digite o valor do veículo: '))
b = float(input('Digite o valor de entrada: '))
c = float(input('Digite o valor da taxa de juros em %: '))
d = float(input('Digite a quantidade de parcelas: '))

exibir = financiamento(a,b,c,d)

print('Valor Total ',exibir)
print('Juros pagos ', round((exibir-a),2))
print('valor da parcela ', round((exibir/d),2))