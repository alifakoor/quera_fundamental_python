n, m = map(int, input().split())
star_number = 0
for i in range(n):
    pic = [obj for obj in input()]
    for obj in pic:
        if obj == '*':
            star_number += 1
print(star_number)