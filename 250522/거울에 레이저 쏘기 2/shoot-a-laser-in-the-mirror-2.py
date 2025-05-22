n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input()) - 1

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
direction = k // n
x, y = 0, 0
ans = 0

for i in range(1, k + 1):
    if i % n == 0:
        continue
    else:
        x += dxs[i // n]
        y += dys[i // n]

print(x, y)

cross = [[0, -1], [-1, 0], [1, 0], [0, 1]]

def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < n

while in_range(x, y):
    ans += 1
    if grid[x][y] == '/':
        if direction == 0:
            x, y = x + cross[0][0], y + cross[0][1]
            direction = 1
        elif direction == 1:
            x, y = x + cross[2][0], y + cross[2][1]
            direction = 0
        elif direction == 2:
            x, y = x + cross[3][0], y + cross[3][1]
            direction = 3
        else:
            x, y = x + cross[1][0], y + cross[1][1]
            direction = 2
    else:
        if direction == 0:
            x, y = x + cross[3][0], y + cross[3][1]
            direction = 3
        elif direction == 1:
            x, y = x + cross[1][0], y + cross[1][1]
            direction = 2
        elif direction == 2:
            x, y = x + cross[0][0], y + cross[0][1]
            direction = 1
        else:
            x, y = x + cross[2][0], y + cross[2][1]
            direction = 0

print(ans)