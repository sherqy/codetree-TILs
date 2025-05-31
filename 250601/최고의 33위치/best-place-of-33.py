n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n - 2):
    for j in range(n - 2):
        cnt = 0
        
        for k in range(i, i + 3):
            cnt += sum(grid[k][j : j + 3])

        ans = max(cnt, ans)

print(ans)