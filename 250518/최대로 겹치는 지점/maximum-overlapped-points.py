n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
line = [0] * 100

for i, j in segments:
    for k in range(i - 1, j + 1):
        line[k] += 1

print(max(line))