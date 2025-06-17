n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    ans = 0

    for i in range(a, b + 1):
        ans += i if i % 2 == 0 else 0

    print(ans)

