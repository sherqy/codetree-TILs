n = int(input())
c = 0

for i in range(1, n + 1):
    if i % 4 == 0 and not (i % 100 == 0 and i % 400 != 0):
        c += 1

print(c)