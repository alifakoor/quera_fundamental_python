n = int(input())
id = []
average = []
number_of_sports = []

def calculate_average(marks):
    return int(sum(marks) / len(marks))

def compare(x, y):
    if average[x] > average[y]:
        return True
    elif average[y] > average[x]:
        return False
    else:
        if number_of_sports[x] > number_of_sports[y]:
            return True
        elif number_of_sports[y] > number_of_sports[x]:
            return False
        else:
            return 'equal'

for i in range(n):
    id.append(input())
    marks = list(map(float, input().split()))
    marks.pop(0)
    average.append(calculate_average(marks))
    sports = list(map(str, input().split()))
    number_of_sports.append(int(sports[0]))

for i in range(1,n):
    for j in range(n-1):
        if compare(j, j+1) == False:
            id[j], id[j+1] = id[j+1], id[j]
            average[j], average[j+1] = average[j+1], average[j]
            number_of_sports[j], number_of_sports[j+1] = number_of_sports[j+1], number_of_sports[j]

for i in range(n):
    print(id[i])