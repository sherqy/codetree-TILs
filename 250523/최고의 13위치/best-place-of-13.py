n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
max_val = 0

# Please write your code here.
for i in range(n):
    for j in range(n - 2):
        max_val = max(max_val, sum(grid[i][j : j + 3]))

print(max_val)