import sys
sys.setrecursionlimit(2500)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
ans = []
count = 0

def in_range(x, y, z):
    return 0 <= x < n and 0 <= y < m and visited[x][y] == False and grid[x][y] - z > 0

def dfs(x, y, z):
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]
    visited[x][y] = True
    count = 1

    for nx, ny in zip(dxs, dys):
        new_x, new_y = x + nx, y + ny

        if in_range(new_x, new_y, z):
            dfs(new_x, new_y, z)

    return count

for k in range(1, 101):
    visited = [[False] * m for _ in range(n)]
    ans_1 = []

    for i in range(n):
        for j in range(m):
            if in_range(i, j, k):
                ans_1.append(dfs(i, j, k))
    if len(ans_1) != 0:
        ans.append(sum(ans_1)) 
    else:
        continue

if len(ans) != 0:
    print(ans.index(max(ans)) + 1, max(ans))
else:
    print(1, 0)