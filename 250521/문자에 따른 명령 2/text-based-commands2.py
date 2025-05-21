dirs = input()

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
direction = 0
x, y = 0, 0

for i in dirs:
    if i == 'L':
        direction = (direction + 3) % 4
    elif i == 'R':
        direction = (direction + 1) % 4
    else:
        x += dx[direction]
        y += dy[direction]

print(x, y)