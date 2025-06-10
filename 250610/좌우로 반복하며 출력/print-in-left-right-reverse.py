n = int(input())
a = list(i + 1 for i in range(n))

for i in range(n):
    if i % 2 == 0:
        print(*a, sep = '')
    else:
        print(*reversed(a), sep = '')