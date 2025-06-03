a = input()

for i in range(len(a)):
    print('a' if i == 1 or i == len(a) - 2 else a[i], end = '')