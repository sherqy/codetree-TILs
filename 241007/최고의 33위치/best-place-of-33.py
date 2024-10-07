n = int(input())
m = list(list(map(int, input().split())) for _ in range(n))
c = []
answer = 0

for k in range(n - 2):
    for i in range(n - 2):
        for j in range(3):
            answer += m[j + k][i : i + 3].count(1)
        c.append(answer)
        answer = 0
print(max(c))