n = int(input())

def f(i):
    if i == 0:
        return 1
    if i == 1:
        return 2
    if i == 2:
        return 4
    return f(i-3) + f(i-2) + f(i-1)

print(f(n))
