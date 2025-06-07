n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
cnt = 0
ans = []

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x, y):
    global cnt
    dxs, dys = [-1, 0, 1, 0], [0, 1, 0, -1]

    for nx, ny in zip(dxs, dys):
        new_x, new_y = x + nx, y + ny

        if in_range(new_x, new_y) and visited[new_x][new_y] == False and grid[new_x][new_y] == 1:
            visited[new_x][new_y] = True
            cnt += 1
            dfs(new_x, new_y)


for i in range(n):
    for j in range(n):
        dfs(i, j)

        if cnt != 0:
            ans.append(cnt)

        cnt = 0

print(len(ans))
print(*sorted(ans), sep = '\n')