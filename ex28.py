# Escreva um programa que calcule e escreva o valor de S

#     1   3   5   7     99
# S = - + - + - + - ... --
#     1   2   3   4     50

s=0
s2=0
i=0
x=1
while i<50:
    i+=1
    print(s,"+",end=" ")
    s+=(x/i)
    s2=(x/i)
    print(f"({x} / {i} = {s2}) = {s}")
    x+=2

print(f"\nS = {s:.2f}\n")
