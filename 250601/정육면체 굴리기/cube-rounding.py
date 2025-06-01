n, m, x, y, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
com = list(map(int, input().split()))

dxs, dys = [0, 0, -1, 1], [1, -1, 0, 0]
cube = [0] * 7
up, front, right = 1, 2, 3

def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < m

for i in com:
    if in_range(x + dxs[i - 1], y + dys[i - 1]):
        x, y = x + dxs[i - 1], y + dys[i - 1]

        if i - 1 == 0:
            cube[right], grid[x][y] = grid[x][y], cube[right]
            up, front, right = 7 - right, front, up
            print(cube[up])
        elif i - 1 == 1:
            cube[7 - right], grid[x][y] = grid[x][y], cube[7 - right]
            up, front, right = right, front, 7 - up
            print(cube[up])
        elif i - 1 == 2:
            cube[7 - front], grid[x][y] = grid[x][y], cube[7 - front]
            up, front, right = front, 7 - up, right
            print(cube[up])
        elif i - 1 == 3:
            cube[front], grid[x][y] = grid[x][y], cube[front]
            up, front, right = 7 - front, up, right
            print(cube[up])