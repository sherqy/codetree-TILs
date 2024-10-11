init = [0, 0]
direction = 0
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
com = input().strip()

for i in com:
    if i == 'L':
        direction += 1
        direction %= 4
    elif i == 'R':
        direction -= 1
        direction %= 4
    else:
        init[0] += dx[direction]
        init[1] += dy[direction]
print(*init)