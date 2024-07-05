# Escreva um algoritmo que solicite ao usuário a entrada de 5 números, e que exiba o somatório
# desses números na tela. Após exibir a soma, o programa deve mostrar também os números que
# o usuário digitou, um por linha.

nums=[]
i=0
while i<5:
    nums.append(float(input("Digite um número: ")))
    i+=1

print(f"\nSoma: {sum(nums)}")
print("\nNúmeros digitados:")
for num in nums:
    print(f"({nums.index(num)+1}) - ",end="")
    print(num)