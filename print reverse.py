def f():
    n = int(input())
    if n != 0:
        f()
        print(n)
f()