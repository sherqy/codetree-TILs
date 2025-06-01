n, m, x, y, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
com = list(map(int, input().split()))

dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]
cube = [0] * 7
up, front, right, bottom = 1, 2, 3, 6

def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < m

for i in com:
    if in_range(x + dxs[i - 1], y + dys[i - 1]):
        x, y = x + dxs[i - 1], y + dys[i - 1]

        if i - 1 == 0:
            up, front, right = 7 - right, front, up
        elif i - 1 == 1:
            up, front, right = right, front, 7 - up
        elif i - 1 == 2:
            up, front, right = front, 7 - up, right
        elif i - 1 == 3:
            up, front, right = 7 - front, up, right

        bottom = 7 - up

        if grid[x][y] == 0:
            grid[x][y] = cube[bottom]
        else:
            grid[x][y], cube[bottom] = 0, grid[x][y]

        print(cube[up])