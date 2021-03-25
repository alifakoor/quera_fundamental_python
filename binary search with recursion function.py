n , q = input().split()
a = list(map(int, input().split()))

def find(l, r, x):
    if (r - l) == 1:
        if a[l] == x:
            return 1
        else:
            return 0
    mid = int((r + l) / 2)
    if x < a[mid]:
        return find(l, mid, x)
    else:
        return find(mid, r, x)

for i in range(int(q)):
    question, number = input().split()
    print(find(0, int(n), int(number)))
