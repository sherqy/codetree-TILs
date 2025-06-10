c1, c2, c3 = 0, 0, 0
n = int(input())

for i in range(1, n + 1):
    if i % 12 == 0:
        c3 += 1
    elif i % 6 == 0:
        c2 += 1
    elif i % 3 == 0:
        c2 += 1
    elif i % 2 == 0:
        c1 += 1

print(c1, c2, c3)