import sys

n = int(input())
a = [int(input()) for _ in range(n)]
min_val = sys.maxsize

# Please write your code here.
for i in range(n):
    dis = 0

    for j in range(n):
        dis += a[j] * j

    a.append(a.pop(0))
    min_val = min(dis, min_val)

print(min_val)