n, t = map(int, input().split())
r, c, d = map(str, input().split())
r, c = int(r), int(c)

direction = {
    'U' : 0,
    'R' : 1,
    'D' : 2,
    'L' : 3
}

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y):
    return x <= n and x >= 1 and y <= n and y >= 1

for i in range(t):
    if in_range(c + dx[direction[d]], r + dy[direction[d]]):
        c, r = c + dx[direction[d]], r + dy[direction[d]]
    else:
        direction = { k : (v + 2) % 4 for k, v in direction.items() }

print(r, c)