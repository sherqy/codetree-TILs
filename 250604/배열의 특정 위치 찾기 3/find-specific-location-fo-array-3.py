a = list(map(int, input().split()))

for i in range(len(a)):
    if a[i] == 0:
        print(a[i - 1] + a[i - 2] + a[i - 3])
        break