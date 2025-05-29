n = int(input())
a, b, c = [], [], []
ans = 0
for _ in range(n):
    num, cnt1, cnt2 = map(int, input().split())
    a.append(num)
    b.append(cnt1)
    c.append(cnt2)

for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or k == i:
                continue
            else:
                suc = True

                for l, m, n in zip(a, b, c):
                    x, y = 0, 0
                    z = [l // 100, (l % 100) // 10, l % 10]
                    
                    if i == z[0]:
                        x += 1
                    if j == z[1]:
                        x += 1
                    if k == z[2]:
                        x += 1
                    if i == z[1] or i == z[2]:
                        y += 1
                    if j == z[0] or j == z[2]:
                        y += 1
                    if k == z[0] or k == z[1]:
                        y += 1

                    if x != m or y != n:
                        suc = False
                        break
                if suc:
                    ans += 1

print(ans)