n, t = map(int, input().split())
r, c, d = input().split()
r, c = int(r), int(c)
mapper = {0 : 'U', 1 : 'R', 2 : 'D', 3 : 'L'}
direction = [i for i, j in mapper.items() if j == d]
drs, dcs = [1, 0, -1, 0], [0, 1, 0, -1]

# Please write your code here.
def in_range(x, y):
    return 1 <= x <= n and 1 <= y <= n

for _ in range(t):
    nr, nc = r + drs[direction[0]], c + dcs[direction[0]]

    if in_range(nr, nc):
        r, c = nr, nc
    else:
        direction[0] = (direction[0] + 2) % 4

print(r, c)