n, x, y = map(int, input().split())
if n % x == 0:
    print(n // x, 0)
else:
    for i in range(n // x):
        result = -1
        rest = n - ((i+1) * x)
        if rest % y == 0:
            result = str(i+1) + ' ' + str(rest // y)
            break
    print(result)