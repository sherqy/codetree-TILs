n = int(input())
ans = 0

for _ in range(n):
    i = int(input())
    ans += i if i % 3 == 0 and i % 2 == 1 else 0

print(ans)