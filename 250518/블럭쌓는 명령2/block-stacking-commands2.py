n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
block = [0] * n

for i, j in commands:
    for l in range(i, j + 1):
        block[l] += 1
        print(block)

print(max(block))