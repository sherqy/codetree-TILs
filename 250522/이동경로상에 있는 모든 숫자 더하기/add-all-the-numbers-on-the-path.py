N, T = map(int, input().split())
str = input()
board = [list(map(int, input().split())) for _ in range(N)]
dxs, dys = [0, -1, 0, 1], [-1, 0, 1, 0]
direction = 1
x, y = (N - 1) // 2, (N - 1) // 2
ans = board[x][y]

def in_range(nx, ny):
    return 0 <= nx < N and 0 <= ny < N

for i in str:
    if i == 'L':
        direction = (direction - 1) % 4
    elif i == 'R':
        direction = (direction + 1) % 4
    else:
        dx, dy = x + dxs[direction], y + dys[direction]

        if in_range(dx, dy):
            x, y = dx, dy
            ans += board[x][y]

print(ans)