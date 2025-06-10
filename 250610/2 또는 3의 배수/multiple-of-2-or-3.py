n = int(input())

for i in range(1, n + 1):
    print(1 if i % 2 == 0 or i % 3 == 0 else 0, end = ' ')
    