n = int(input())
ans = 0

for i in range(1, n + 1):
    ans += 1 if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 else 0

print(n - ans)