n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

def can_go(x, y):
    return 0 <= x < n and 0 <= y < m and grid[x][y] == 1 and visited[x][y] != True

def dfs(x, y):
    dxs, dys = [1, 0], [0, 1]

    if x == n - 1 and y == m - 1:
        return True

    for nx, ny in zip(dxs, dys):
        nnx, nny = x + nx, y + ny

        if can_go(nnx, nny):
            visited[nnx][nny] = True
            if dfs(nnx, nny):
                return True

    return False

print(1 if dfs(0, 0) else 0)