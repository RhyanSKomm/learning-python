# Elabore um algoritmo para fazer cálculo de potenciação. Ou seja, x^y. (Exemplo: 3^4 = 3 x 3 x 3
# x 3). Seu algoritmo deverá solicitar que o usuário entre com o valor da base (x) e do expoente
# (y) e apresentar o resultado do cálculo sem utilizar os operadores (por exemplo **). Para
# resolver o problema utilize estrutura de repetição.

base=int(input("Digite o valor da base: "))
expoente=int(input("Digite o valor do expoente: "))
i=1
potencia=base
while i<expoente:
    i+=1
    potencia*=base
print(f"{base}^{expoente} = {potencia}")