n = int(input())
numbers = list(map(int, input().split()))
for i in range(1,n):
    for j in range(n-1):
        if numbers[j+1] > numbers[j]:
            numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
for k in range(n):
    print(numbers[k], end=' ')