a, b = map(int, input().split())
ans = 0
v = 0

for i in range(a, b + 1):
    if i % 5 == 0 or i % 7 == 0:
        v += 1
        ans += i

print(ans, f"{ans / v:.1f}")