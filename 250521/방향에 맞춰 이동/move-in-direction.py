n = int(input())
moves = [tuple(input().split()) for _ in range(n)]
dir = [move[0] for move in moves]
dist = [int(move[1]) for move in moves]

# Please write your code here.
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
x, y = 0, 0

for i, j in zip(dir, dist):
    if i == 'N':
        y += dy[3] * j
    elif i == 'S':
        y += dy[1] * j
    elif i == 'E':
        x += dx[0] * j
    else:
        x += dx[2] * j

print(x, y)