n = int(input())

def gcd(a, b):
    if a > b:
        a, b = b, a
    while a > 0:
        b = b % a
        a, b = b, a
    return b

def lcm(a, b):
    return int((a * b) / gcd(a, b))

result = 1
for i in range(1, n):
    if gcd(i, n) == 1:
        result = lcm(result, i)
print(result)