x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Please write your code here.
cross = [[0] * 2001 for _ in range(2002)]
ans = 0

for i in range(3):
    if i != 2:
        for j in range(x1[i] + 1000, x2[i] + 1000):
            for k in range(y1[i] + 1000, y2[i] + 1000):
                cross[j][k] = 1
    else:
        for j in range(x1[i] + 1000, x2[i] + 1000):
            for k in range(y1[i] + 1000, y2[i] + 1000):
                cross[j][k] = 0

for i in cross:
    ans += i.count(1)

print(ans)