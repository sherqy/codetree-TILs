n = int(input())
grid = [[0] * n for _ in range(n)]
x, y = n - 1, n
dxs, dys = [0, -1, 0, 1], [-1, 0, 1, 0]
direction = 0
i = n * n

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

while i > 0:
    dx, dy = x + dxs[direction], y + dys[direction]

    if in_range(dx, dy) and grid[dx][dy] == 0:
        x, y = dx, dy
        grid[dx][dy] = i
        i -= 1
    else:
        direction = (direction + 1) % 4

for i in grid:
    print(*i)