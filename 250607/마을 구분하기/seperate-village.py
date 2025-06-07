n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [[0]*n for _ in range(n)]

cnt = 0
people = []

def dfs(x, y):
    global cnt
    visited[x][y] = 1
    cnt += 1

    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if can_go(new_x, new_y):
            dfs(new_x, new_y)

def can_go(x, y):
    if x >= n or y >= n:
        return False
    if visited[x][y] or grid[x][y] == 0:
        return False
    if x < 0 or y < 0: 
        return False
    return True


for i in range(n):
    for j in range(n):
        if can_go(i, j):
            cnt = 0
            dfs(i, j)
            people.append(cnt)

people.sort()
print(len(people))
for i in range(len(people)):
    print(people[i])
