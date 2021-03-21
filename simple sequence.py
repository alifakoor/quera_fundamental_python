n = int(input())

def f(i):
    if i == 0:
        return 5
    if i % 2 == 0:
        return f(i-1)-21
    if i % 2 != 0:
        return f(i-1)*f(i-1)

print(f(n))