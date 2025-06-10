n = int(input())

for i in range(1, n + 1):
    j = list(str(i))
    if i % 3 == 0 or '3' in j or '6' in j or '9' in j:
        print(0, end = ' ')
    else:
        print(i, end = ' ')