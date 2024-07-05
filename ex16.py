def tri(n):
    for i in range(n+1):
        print('*'*i)
    for j in range(n-1,n-n,-1):
        print('*'*j)
tri(4)