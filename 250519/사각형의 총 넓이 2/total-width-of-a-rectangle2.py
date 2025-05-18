n = int(input())
pos = []
for _ in range(n):
    pos.append(list(map(int, input().split())))

# Please write your code here.
cross = [[0] * 201 for _ in range(202)]
ans = 0

for a, b, c, d in pos:
    for i in range(a + 100, c + 100):
        for j in range(b + 100, d + 100):
            cross[i][j] = 1

for i in cross:
    ans += i.count(1)

print(ans)