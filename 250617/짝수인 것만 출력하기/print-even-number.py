n = int(input())
m = list(map(int, input().split()))

for i in m:
    if i % 2 == 0:
        print(i, end = ' ')