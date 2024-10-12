from collections import deque

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
visited = [
    [False for _ in range(n)] for _ in range(n)
]
weight = [
    [0 for _ in range(n)] for _ in range(n)
]

q = deque()

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def push(x, y, s):
    visited[y][x] = True
    weight[y][x] = s + 1
    q.append((x, y))

def bfs():
    dxs, dys = [-2, -2, -1, -1, 1, 1, 2, 2], [-1, 1, -2, 2, -2, 2, -1, 1]

    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if in_range(new_x, new_y) and not visited[new_y][new_x]:
                push(new_x, new_y, weight[y][x])

push(r1 - 1, c1 - 1, 0)
bfs()
print(weight[r2 - 1][c2 - 1] - 1)