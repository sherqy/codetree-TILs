n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if j % 2 == 1:
            print(i, end = '')
        else:
            print(n + 1 - i, end = '')
    print()