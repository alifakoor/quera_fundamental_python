x = [char for char in input()]
num = int(''.join(x))
n = len(x)
index = list(range(n))
cycle = list(range(n, 0, -1))
result = []
while n:
    for i in reversed(range(n)):
        cycle[i] -= 1
        if cycle[i] == 0:
            index[i:] = index[i+1:] + index[i:i+1]
            cycle[i] = n - i
        else:
            j = cycle[i]
            index[i], index[-j] = index[-j], index[i]
            helper = int(''.join(tuple(x[i] for i in index[:n])))
            if helper > num:
                result.append(helper)
            break
    else:
        break
if not len(result):
    print(0)
else:
    print(min(result))