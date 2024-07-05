def salario(a,b):
    if b == 0:
        return a
    else:
        c = 0
        for i in range(b):
            d = a*0.5
            c+=d
        e = a+c
        return e
            

       


n1 = float(input('Digite o saário: '))
n2 = int(input('Quantas hrs a mais foram trabalhadas?  '))

print(salario(n1,n2))