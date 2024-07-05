# O funcionário chamado Carlos tem um colega chamado João que recebe um salário que é
# equivale a um terço do seu salário. Carlos gosta de fazer aplicações na caderneta de poupança
# e vai aplicar seu salário integralmente nela, pois está rendendo 2% ao mês. João irá aplicar seu
# salário integralmente no fundo de renda fixa, que está rendendo 5% ao mês. Construa um
# programa que deverá calcular e mostrar a quantidade de meses necessários para que o valor
# pertencente a João iguale ou ultrapasse o valor pertencente a Carlos. Teste com outros valores
# para as taxas.

sal_carlos=float(input("\nDigite o valor do salário de Carlos: "))
sal_joao=sal_carlos/3
meses=0

while sal_joao<sal_carlos:
    sal_carlos+=(sal_carlos*0.02)
    sal_joao+=(sal_joao*0.05)
    meses+=1

print(f"\nSalário de Carlos: R${sal_carlos:.2f}")
print(f"Salário de João: R${sal_joao:.2f}")
print(f"Meses necessários para os salários se igualarem: {meses}\n")