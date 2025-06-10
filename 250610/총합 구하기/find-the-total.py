a, b = map(int, input().split())
ans = 0

for i in range(a, b + 1):
    ans += i if i % 6 == 0 and i % 8 != 0 else 0

print(ans)