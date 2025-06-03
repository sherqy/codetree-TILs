n = int(input())
a = ''.join(list(input().split()))

for i in range(len(a)):
    if i % 5 != 0 and i == 0:
        print(a[i], end = '')
    else:
        print()
        print(a[i], end = '')