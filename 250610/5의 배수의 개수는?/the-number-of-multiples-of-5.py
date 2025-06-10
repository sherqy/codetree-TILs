ans = 0

for i in range(4):
    a = list(map(int, input().split()))

    for i in a:
        if i % 5 == 0:
            ans += 1

print(ans)