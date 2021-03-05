n, t = input().split()
for i in range(int(n)):
    code = input()
    fail = False
    for j in t:
        found = False
        for k in code:
            if j == k:
                found = True
        if not found:
            fail = True
    
    for j in code:
        found = False
        for k in t:
            if j == k:
                found = True
        if not found:
            fail = True

    if fail:
        print('No')
    else:
        print('Yes')