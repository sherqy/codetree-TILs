N = int(input())
moves = [tuple(input().split()) for _ in range(N)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
time = 0
flag = 0

def is_start(dx, dy):
    return x == 0 and y == 0

# Please write your code here.
for i, j in zip(dir, dist):
    if i == 'N':
        for _ in range(j):
            y += 1
            time += 1
            if is_start(x, y) and flag == 0:
                print(time)
                flag += 1
    elif i == 'E':
        for _ in range(j):
            x += 1
            time += 1
            if is_start(x, y) and flag == 0:
                print(time)
                flag += 1
    elif i == 'S':
       for _ in range(j):
            y -= 1
            time += 1
            if is_start(x, y) and flag == 0:
                print(time)
                flag += 1
    else:
        for _ in range(j):
            x -= 1
            time += 1
            if is_start(x, y) and flag == 0:
                print(time)
                flag += 1

if flag == 0:
    print(-1)