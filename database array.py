n = int(input())
input = [
    ['+','1','1'],
    ['+', '2', '3'],
    ['+', '2', '10'],
    ['+', '4', '5'],
    ['+', '2', '100'],
    ['-', '2'],
    ['-', '2']
]
arr = []

for i in range(n):
    # row = list(map(str, input().split()))
    row = input[i]
    arr_len = len(arr)
    if row[0] == '+':        
        if arr_len <= (int(row[1])-1):
            arr.append(int(row[2]))
        elif arr_len > (int(row[1])-1):
            arr.append(0)
            for j in range(arr_len, int(row[1])-1, -1):
                arr[j], arr[j-1] = arr[j-1], arr[j]
            arr[int(row[1])-1] = int(row[2])
        
        for z in range(arr_len+1):
            if z == (arr_len):
                print(arr[z])
            else:
                print(arr[z], end=' ')
        
    elif row[0] == '-':
        arr.pop(int(row[1])-1)
        arr_len -= 1
        if arr_len != 0:
            for z in range(arr_len):
                if z == (arr_len-1):
                    print(arr[z])
                else:
                    print(arr[z], end=' ')
        else:
            print('EMPTY')