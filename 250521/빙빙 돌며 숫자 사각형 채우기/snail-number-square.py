n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
arr[0][0] = 1

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
direction = 0
x, y = 0, 0

# Please write your code here.
def in_range(x, y):
    return 0 <= x < n and 0 <= y <m

for i in range(2, n * m + 1):
    nx, ny = x + dxs[direction], y + dys[direction]
    if in_range(nx, ny) and arr[nx][ny] == 0:
        arr[nx][ny] = i
        x, y = nx, ny
    else:
        direction = (direction + 1) % 4
        nx, ny = x + dxs[direction], y + dys[direction]
        arr[nx][ny] = i
        x, y = nx, ny
    

for i in arr:
    print(*i)