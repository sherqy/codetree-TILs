import sys

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
ans = 1600000000

for i in range(n):
    x_min = sys.maxsize
    y_min = sys.maxsize
    x_max = -sys.maxsize
    y_max = -sys.maxsize

    for j in range(len(points)):
        if i == j:
            continue
        else:
            x_min = min(x_min, points[j][0])
            x_max = max(x_max, points[j][0])
            y_min = min(y_min, points[j][1])
            y_max = max(y_max, points[j][1])

    ans = min(ans, (y_max - y_min) * (x_max - x_min))

print(ans)