n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ans = 0

for i in range(n):
    
    cnt = 1
    max_val = 1
    for j in range(n - 1):
        if grid[i][j] == grid[i][j + 1]:
            cnt += 1
        else:
            max_val = max(max_val, cnt)
            cnt = 1
    max_val = max(max_val, cnt)
    ans += 1 if max_val >= m else 0
    

    cnt = 1
    max_val = 1
    for j in range(n - 1):
        if grid[j][i] == grid[j + 1][i]:
            cnt += 1
        else:
            max_val = max(max_val, cnt)
            cnt = 1
    max_val = max(max_val, cnt)
    ans += 1 if max_val >= m else 0

print(ans)