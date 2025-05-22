n, m = map(int, input().split())
grid = [[0] * m for _ in range(n)]
x, y = -1, 0
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
i = 1
direction = 0

# Please write your code here.
def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < m

while i <= n * m:
    dx, dy = x + dxs[direction], y + dys[direction]
    
    if in_range(dx, dy) and grid[dx][dy] == 0:
        grid[dx][dy] = i
        x, y = dx, dy
        i += 1
    else:
        direction = (direction + 1) % 4


for i in grid:
    print(*i)