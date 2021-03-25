n = int(input())

seen = [[0 for k in range(n)] for z in range(n)]
value = [[0 for k in range(n)] for z in range(n)]

def f(i, j):
    if seen[i][j] == 1:
        return value[i][j]
    seen[i][j] = 1
    if i == j or j == 0:
        value[i][j] = 1
    else:
        value[i][j] = f(i-1, j) + f(i-1, j-1)
    return value[i][j]

for i in range(n):
    for j in range(i+1):
        print(f(i, j), end=' ')
    print('')