n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
ans = []

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n and visited[x][y] == False and grid[x][y] == 1

def dfs(x, y):
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    visited[x][y] = True
    count = 1

    for nx, ny in zip(dxs, dys):
        new_x, new_y = x + nx, y + ny

        if in_range(new_x, new_y):
            count += dfs(new_x, new_y)

    return count


for i in range(n):
    for j in range(n):
        if in_range(i, j):
            ans.append(dfs(i, j))

print(len(ans))
print(*sorted(ans), sep = '\n')