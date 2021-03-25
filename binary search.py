n , q = input().split()
a = list(map(int, input().split()))

def find(l, r, x):
    while (r - l) > 1:
        mid = int((r + l) / 2)
        if x < a[mid]:
            r = mid
        else:
            l = mid
    if a[l] == x:
        return 1
    else:
        return 0

for i in range(int(q)):
    question, number = input().split()
    print(find(0, int(n), int(number)))
