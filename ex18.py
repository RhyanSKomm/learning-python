def gerar_triangulo(n):
    for i in range(1, n + 1):
        espacos = ' ' * (n - i)  
        asteriscos = '*' * (2 * i - 1) 
        print(espacos + asteriscos)

n = 6
gerar_triangulo(n)