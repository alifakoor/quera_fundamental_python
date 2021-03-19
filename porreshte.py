n = int(input())
strings = ['']*100
res = []
for i in range(n):
    command = [char for char in input().split()]
    if command[0] == '1':
        strings[int(command[1])-1] += command[3]
    elif command[0] == '2':
        index_str = [char for char in strings[int(command[1])-1]]
        s = command[3]
        result = 0
        for j in range(len(index_str)):
            helper = []
            for k in range(len(s)):
                if k+j < len(index_str):
                    helper.append(index_str[(k+j) % len(index_str)])
            if ''.join(helper) == s:
                result += 1
        res.append(result)
for x in res:
    print(x)