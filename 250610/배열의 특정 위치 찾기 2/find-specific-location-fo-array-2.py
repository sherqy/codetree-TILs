a = list(map(int, input().split()))
v1, v2 = 0, 0

for i in range(len(a)):
    if i % 2 == 1:
        v1 += a[i]
    else:
        v2 += a[i]

print(max(v1, v2) - min(v1, v2))