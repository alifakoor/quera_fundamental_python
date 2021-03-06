n = int(input())
max_word = 0
for i in range(n):
    name = [char for char in input()]
    helper = []
    max_char = 0
    for j in range(len(name)):
        if name[j] not in helper:
            helper.append(name[j])
            max_char += 1
    if max_word < max_char:
        max_word = max_char
print(max_word)