start, end = map(int, input().split())
ans = 0

for i in range(start, end + 1):
    cnt = 0
    for j in range(1, i + 1):
        cnt += 1 if i % j == 0 else 0
    ans += 1 if cnt == 3 else 0

print(ans)