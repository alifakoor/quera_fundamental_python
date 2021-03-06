n = 20
colors = [1, 2, 2, 3, 4, 1, 5, 9, 9, 65, 65, 58, 1, 58, 62, 62, 3, 4, 5, 100]
counter = [0]*101
max_color = 0
for i in range(n):
    counter[colors[i]] += 1
    if colors[i] > max_color:
        max_color = colors[i]

answer = -1
for i in range(max_color+1):
    if counter[i] > 0:
        if answer == -1 or counter[answer] > counter[i] or (counter[answer] == counter[i] and i < answer):
            answer = i
print(answer)