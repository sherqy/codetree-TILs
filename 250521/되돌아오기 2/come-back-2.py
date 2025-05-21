commands = input()
direction = 0
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0
flag = 0

for i in range(len(commands)):
    if commands[i] == 'L':
        direction = (direction + 3) % 4
    elif commands[i] == 'R':
        direction = (direction + 1) % 4
    else:
        x, y = x + dxs[direction], y + dys[direction]
        flag += 1

    if x == 0 and y == 0 and flag != 0:
        print(i + 1)
        break
    if i == len(commands) - 1:
        print(-1)