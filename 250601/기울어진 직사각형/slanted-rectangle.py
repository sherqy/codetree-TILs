n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [1, 1, -1, -1], [1, -1, -1, 1]
ans = 0

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def make(x, y):
    arr = []
    direction = 0
    cnt = 0

    while len(arr) != 4:
        if not in_range(x + dxs[direction], y + dys[direction]):
            arr.append(cnt)
            direction += 1
            cnt = 0
        else:
            cnt += grid[x][y]
            x += dxs[direction]
            y += dys[direction]

    return sum(arr) if 0 not in arr else 0
    
for i in range(n):
    for j in range(n):
        ans = max(ans, make(i, j))

print(ans)