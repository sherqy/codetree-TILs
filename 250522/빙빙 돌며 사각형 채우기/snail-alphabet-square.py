n, m = map(int, input().split())
alp = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
x, y = 0, -1
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
grid = [[''] * m for _ in range(n)]
direction = 0

def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < m

for i in range(n * m):
    dx, dy = x + dxs[direction], y + dys[direction]

    if in_range(dx, dy) and grid[dx][dy] == '':
        grid[dx][dy] = alp[i % 26]
        x, y = dx, dy
    else:
        direction = (direction + 1) % 4
        dx, dy = x + dxs[direction], y + dys[direction]
        grid[dx][dy] = alp[i % 26]
        x, y = dx, dy

for i in grid:
    print(*i)