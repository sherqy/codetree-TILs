n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Please write your code here.
cross = [[0] * 201 for _ in range(202)]
ans = 0

for i in range(n):
    for j in range(8):
        for k in range(8):
            cross[x[i] + j + 100][y[i] + k + 100] = 1

for i in cross:
    ans += i.count(1)

print(ans)