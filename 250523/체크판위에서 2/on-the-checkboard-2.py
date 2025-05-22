R, C = map(int, input().split())
grid = [list(input().split()) for _ in range(R)]

# Please write your code here.
start = grid[0][0]
ans = 0

for i in range(1, R - 1):
    for j in range(1, C - 1):
        if start != grid[i][j]:
            for k in range(i + 1, R - 1):
                for l in range(j + 1, C - 1):
                    if start == grid[k][l]:
                        ans += 1

print(ans)