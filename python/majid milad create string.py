l, r = map(int, input().split())
string = '1'
helper = string
result = ''
while (len(string) < r):
    for char in string:
        if char == '1':
            helper += '0'
        else:
            helper += '1'
    string = helper
for i in range(len(string)):
    if i >= l-1 and i < r:
        result += string[i]
print(result)