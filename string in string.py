s = input()
p = input()
for i in range(len(s)):
    flag = True
    for j in range(len(p)):
        if i + j < len(s):
            if s[i + j] != p[j]:
                flag = False
        else:
            flag = False
    if flag:
        print(i + 1, end=' ')
