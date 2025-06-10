import sys

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
ans = sys.maxsize

for i in range(len(points) - 1):
    for j in range(i + 1, len(points)):
        ans = min(ans, (points[i][0] - points[j][0]) ** 2 + (points[i][1] - points[j][1]) ** 2)

print(ans)