# Chico tem 1.70 metro e cresce 2 centímetros por ano, enquanto Zé tem 1.20 metros e cresce 3
# centímetros por ano. Escreva um programa que calcule e imprima quantos anos serão
# necessários para que Zé seja maior que Chico.

alt_chico=float(1.70)
alt_ze=float(1.20)
anos=0

while alt_ze<alt_chico:
    alt_chico+=0.02
    alt_ze+=0.03
    anos+=1

print(f"\nAltura do Chico: {alt_chico:.2f}")
print(f"Altura do Zé: {alt_ze:.2f}")
print(f"Anos necessários para que Zé seja maior que Chico: {anos}\n")