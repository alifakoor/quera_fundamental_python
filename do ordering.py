n, k = map(int, input().split())
numbers = list(map(int, input().split()))

def order_arrays(lenght, array):
    for i in range(lenght):
        min_index = i
        for j in range(i, lenght):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]
    return array

numbers = order_arrays(n, numbers)
print(numbers)
answer = 999999999999
for i in range(n):
    counter = 1
    p = i + 1
    while p < n:
        if numbers[p] != numbers[p-1]:
            counter += 1
        if counter == k:
            answer = min(answer, abs(numbers[p] - numbers[i]))
            break
        p += 1
if answer == 999999999999 or answer == 0:
    print(-1)
else:
    print(answer)