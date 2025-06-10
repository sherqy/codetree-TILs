n = int(input())
ans = 0

for i in range(1, n // 2 + 1):
    if n % i == 0:
        ans += i

print("P" if ans == n else "N")