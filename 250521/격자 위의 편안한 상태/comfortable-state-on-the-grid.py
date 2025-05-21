n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
grid = [[0] * n for _ in range(n)]

def in_range(x, y):
    return 1 <= x < n - 1 and 1 <= y < n - 1

for i, j in points:
    grid[i - 1][j - 1] = 1
    count = 0

    if in_range(i - 1, j - 1):
        for k, l in zip(dxs, dys):
            if grid[i + k - 1][j + l - 1] == 1:
                count += 1

    if count == 3:
        print(1)
    else:
        print(0)