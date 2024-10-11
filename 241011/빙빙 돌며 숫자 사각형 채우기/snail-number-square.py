n, m = map(int, input().split())
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
snail = list([0] * m for _ in range(n))
direction = 0
pos_x, pos_y = 0, 0
flag = 1

def in_range(x, y):
    return x >= 0 and x < m and y >= 0 and y < n

while flag <= n * m:
    if in_range(pos_x, pos_y) and snail[pos_y][pos_x] == 0:
        snail[pos_y][pos_x] = flag
        pos_y, pos_x = pos_y + dys[direction], pos_x + dxs[direction]
        flag += 1
        
    else:
        pos_x, pos_y = pos_x - dxs[direction], pos_y - dys[direction]
        direction = (direction + 1) % 4
        pos_y, pos_x = pos_y + dys[direction], pos_x + dxs[direction]

for i in snail:
    print(*i)