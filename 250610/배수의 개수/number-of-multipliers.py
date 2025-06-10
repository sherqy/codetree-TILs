c1 = 0
c2 = 0

for _ in range(10):
    i = int(input())

    if i % 3 == 0:
        c1 += 1
    if i % 5 == 0:
        c2 += 1

print(c1, c2)