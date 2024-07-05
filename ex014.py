m1 = [[1, 13, 3],
      [4, 45,67],
      [7, 80, 9]]

m2 = [[100,8,7],
      [6, 5, 4 ],
      [3, 25,10]]

nl = []

for i in range(len(m1)):
    l = []
    for j in range(len(m1[0])):
        l.append((m1[i][j])+(m2[i][j]))
    nl.append(l)

print(nl)