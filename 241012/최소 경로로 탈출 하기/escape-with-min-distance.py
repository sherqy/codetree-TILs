from collections import deque

n, m = map(int, input().split())
track = [
    list(map(int, input().split())) for _ in range(n)
]
visited = [
    [False for _ in range(m)] for _ in range(n)
]
weight = [
    [0 for _ in range(m)] for _ in range(n)
]
q = deque()

def in_range(x, y):
    return x >= 0 and x < m and y >= 0 and y < n

def push(new_x, new_y, x, y):
    if track[new_y][new_x] == 1:
        weight[new_y][new_x] += weight[y][x] + track[new_y][new_x]
        visited[new_y][new_x] = True
        q.append((new_x, new_y))

def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            if in_range(new_x, new_y) and track[new_y][new_x] != 0 and not visited[new_y][new_x]:
                push(new_x, new_y, x, y)
   
push(0, 0, 0, 0)
bfs()
print(weight[n - 1][m - 1] - 1)