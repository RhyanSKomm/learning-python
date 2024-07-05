# Um funcionário recebe aumento anual. Em 2019 foi contratado por 4000 reais. Em 2020
# recebeu aumento de 1.5%. A partir de 2021, os aumentos sempre correspondem ao dobro do
# ano anterior. Faça um programa que determine o salário atual do funcionário.

sal=4000
aumento=0.015
for i in range(2020,2024+1):
    sal=sal+(sal*aumento)
    aumento*=2

print(f"Salário atual: R${sal:.2f}")