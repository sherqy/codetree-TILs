n = int(input())
ans = 0

for _ in range(n):
    ans += int(input())

print(ans, f"{ans / n:.1f}")