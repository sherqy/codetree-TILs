def in_range(x, y):
    return x <= n - 1 and x >= 0 and y <= n - 1 and y >= 0

n = int(input())
m = list(list(map(int, input().split())) for _ in range(n))
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
answer = 0

for i in range(n):
    for j in range(n):
        count = 0
        for x, y in zip(dxs, dys):
            if in_range(x + j, y + i) and m[x + j][y + i] == 1:
                count += 1
        if count >= 3:
            answer += 1

print(answer)