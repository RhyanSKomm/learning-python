# Faça um programa que calcule a diferença entre a soma dos quadrados dos primeiros 100
# números naturais e o quadrado da soma. Ex: A soma dos quadrados dos dez primeiros números
# naturais e,

# 1^2 + 2^2 + ... + 10^2 = 385

# O quadrado da soma dos dez primeiros números naturais é,

# (1 + 2 + ... + 10)^2 = 552 = 3025

# A diferença entre a soma dos quadrados dos dez primeiros números naturais e o quadrado da
# soma e 3025-385 = 2640.

soma_prim=0
soma_quad=0
x=0

while x<100:
    x+=1
    soma_prim+=(x**2)
    soma_quad+=x
    
soma_quad=soma_quad**2

print(f"A diferença entre a soma dos quadrados dos cem primeiros números naturais e o quadrado da soma é:\n {soma_quad} - {soma_prim} = {soma_quad-soma_prim}.")