n, k = map(int, input().split())
names = []
results = []

for i in range(n):
    names.append(input())

def compare(name1, name2):
    min_len = len(name1)
    if min_len > len(name2):
        min_len = len(name2)
    for i in range(min_len):
        if ord(name1[i]) > ord(name2[i]):
            return False
        elif ord(name2[i]) > ord(name1[i]):
            return True
        else:
            continue

for i in range(n-1):
    min_index = i
    for j in range(i, n):
        if compare(names[j], names[min_index]):
            min_index = j
    names[i], names[min_index] = names[min_index], names[i]

for i in range(n):
    results.append(''.join(names[i][:k]))

print(results.count(max(set(results), key = results.count)))