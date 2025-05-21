n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
grid = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

for i, j in points:
    grid[i - 1][j - 1] = 1
    count = 0

    for k, l in zip(dxs, dys):
        if in_range(i + k - 1, j + l - 1) and grid[i + k - 1][j + l - 1] == 1:
            count += 1

    if count == 3:
        print(1)
    else:
        print(0)