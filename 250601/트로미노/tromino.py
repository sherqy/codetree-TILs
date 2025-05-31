n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0

def nieun(x, y):
    z = grid[x][y] + grid[x][y + 1] + grid[x + 1][y] + grid[x + 1][y + 1]
    max_val = 0

    for a, b in zip([0, 1], [0, 1]):
        max_val = max(max_val, z - grid[x + a][y + b])

    return max_val

for i in range(n - 1):
    for j in range(m - 1):
        ans = max(nieun(i, j), ans)

for i in range(n - 2):
    for j in range(m - 2):
            for k in range(3):
                ans = max(ans, sum(grid[i + k][j : j + 3]), grid[i][j + k] + grid[i + 1][j + k] + grid[i + 2][j + k])

print(ans)