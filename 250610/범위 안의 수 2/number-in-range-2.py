ans = 0
v = 0

for _ in range(10):
    i = int(input())

    if 0 <= i <= 200:
        ans += i
        v += 1

print(ans, f"{ans / v:.1f}")