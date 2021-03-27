def f(n1):
    global sm, ans
    if n1 == 0:
        return
    x = int(input())
    sm += x
    f(n1 - 1)
    if x > sm // n:
        ans += x - sm // n
ans = 0
sm = 0
n = int(input())
f(n)
print(ans)
