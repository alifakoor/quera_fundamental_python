q = int(input())
wallet = []

def ordering(n, array):
    for i in range(1, n):
        p = i
        while p > 0 and array[p] < array[p-1]:
            array[p], array[p-1] = array[p-1], array[p]
            p -= 1
    return array

for i in range(q):
    command = list(input().split())
    if command[0] == 'Add':
        wallet.append(int(command[1]))
        wallet = ordering(len(wallet), wallet)
    elif command[0] == 'Ask':
        print(wallet[int(command[1])-1])
