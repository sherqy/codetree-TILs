ans = 0

for _ in range(10):
    a = int(input())

    if a % 3 == 0 or a % 5 == 0:
        ans += 1

print(ans)