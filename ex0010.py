M=[]
for i in range (5):
    l=[]
    for j in range (5):
        if i == j:
           l.append(1)
        else:
           l.append(0)
    M.append(l)

for i in M:
    print(i)
