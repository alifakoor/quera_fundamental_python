n = int(input())
fibonacchi_sequence = [0]*(n+1)
for i in range(1, n+1):
    if i == 1 or i == 2:
        fibonacchi_sequence[i] = i
        print('+', end='')
    else:
        fibonacchi_sequence[i] = fibonacchi_sequence[i-1] + fibonacchi_sequence[i-2]
        if i in fibonacchi_sequence:
            print('+', end='')
        else:
            print('-', end='')