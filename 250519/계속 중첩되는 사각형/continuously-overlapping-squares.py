n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.
cross = [[0] * 201 for _ in range(202)]
ans = 0

for i in range(n):
    if i % 2 == 0:
        for j in range(x1[i] + 100, x2[i] + 100):
            for k in range(y1[i] + 100, y2[i] + 100):
                cross[j][k] = 1
    else:
        for j in range(x1[i] + 100, x2[i] + 100):
            for k in range(y1[i] + 100, y2[i] + 100):
                cross[j][k] = 2

for i in cross:
    ans += i.count(2)

print(ans)