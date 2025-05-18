n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
line = [0] * 200

for i, j in segments:
    for k in range(i + 99, j + 99):
        line[k] += 1

print(max(line))