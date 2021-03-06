n, m = map(int, input().split())
arr = []
for i in range(n):
    string = [char for char in input()]
    arr.append(string)
s = [char for char in input()]
size = len(s)
result = 0
for i in range(n):
    for j in range(m-size+1):
        diff = 0
        for k in range(size):
            if s[k] != arr[i][k+j]:
                diff = 1
        if diff == 0:
            result += 1
for i in range(n-size+1):
    for j in range(m):
        diff = 0
        for k in range(size):
            if s[k] != arr[i+k][j]:
                diff = 1
        if diff == 0:
            result += 1
print(result)