a = list(map(int, input().split()))
b = 0
c = 0

for i in range(10):
    if (i + 1) % 2 == 0:
        b += a[i]
    if (i + 1) % 3 == 0:
        c += a[i]

print(f"{b} {c / 3:.1f}")