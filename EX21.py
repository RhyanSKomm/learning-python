n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

sum = 0

mult = 1

for i in range (n1, n2+1):
    if i % 2 == 0:
        sum += i

for j in range (n1,n2+1):
    if j %2 == 1:
        mult *= j

print(sum,mult)