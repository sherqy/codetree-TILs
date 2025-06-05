n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
grid = [[0] * n for _ in range(n)]
visited = [False] * n

for i, j in edges:
    grid[i - 1][j - 1] = 1
    grid[j - 1][i - 1] = 1

def dfs(x):
    a = 0
    for curr in range(n):
        if grid[x][curr] == 1 and not visited[curr]:
            visited[curr] = True
            a = a + 1 + dfs(curr)
    
    return a if a > 0 else 0

if dfs(0) == 0:
    print(0)
else:
    print(dfs(0) - 1)