n = int(input())

def hanoi(az, to, help, n, move):
    if n == 1:
        move += 1
        print(move, az, to)
        return move
    else:
        h = hanoi(az, help, to, n-1, move)
        move = h
        move += 1
        print(move, az, to)
        h = hanoi(help, to, az, n-1, move)
        move = h
        return move

hanoi('A', 'B', 'C', n, 0)