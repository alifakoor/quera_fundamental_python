s = [char for char in input()]
p = input()
result = 'No'
for i in range(len(s)):
    helper = []
    for j in range(len(p)):
        helper.append(s[j % len(s)])
    if ''.join(helper) == p:
        result = 'Yes'
    s.append(s[0])
    s.pop(0)
print(result)