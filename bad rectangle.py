n = int(input())
result = 0
for i in range(1, (n // 3) + 1):
    result = result + (((n - 3 * i) // 2) - max(0, ((n // 2) - (2 * i) + 1))) + 1
print(result)