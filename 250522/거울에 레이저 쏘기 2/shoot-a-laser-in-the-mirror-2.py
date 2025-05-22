n = int(input())
grid = [list(input()) for _ in range(n)]
k = int(input()) - 1

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
direction = (k // n + 1) % 4
x, y = 0, 0
ans = 0

for i in range(0, k + 1):
    if i % n == 0:
        continue
    else:
        x += dxs[i // n]
        y += dys[i // n]
    
def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < n

def move(x, y, move_dir):
    global dxs, dys
    if not (0 <= move_dir < 4):
        print(move_dir)
    return x + dxs[move_dir], y + dys[move_dir], move_dir

while in_range(x, y):
    ans += 1
    if grid[x][y] == '\\':
        x, y, direction = move(x, y, direction ^ 1)
    else:
        x, y, direction = move(x, y, 3 - direction)

print(ans)