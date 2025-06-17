n = int(input())
arr = [1, n]
i = 0

while i < 100:
    i = arr[-1] + arr[-2]
    arr.append(i)

print(*arr, end = ' ')