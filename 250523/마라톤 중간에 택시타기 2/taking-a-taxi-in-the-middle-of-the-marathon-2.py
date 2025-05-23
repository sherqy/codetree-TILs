import sys

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
skip_x = 0
skip_y = 0
min_val = sys.maxsize

for i in range(1, len(points) - 1):
    x, y = points.pop(i)
    dis = 0

    for j in range(len(points) - 1):
        dis += abs(points[j][0] - points[j + 1][0]) + abs(points[j][1] - points[j + 1][1])

    min_val = min(min_val, dis)
    points.insert(i, (x, y))

print(min_val)