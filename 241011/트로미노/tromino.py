import sys
input = sys.stdin.readline

n, m = map(int, input().split())
k = list(list(map(int, input().split())) for _ in range(n))
answer = 0

for i in range(n):
    for j in range(m):
        if i <= n - 3:  #세로 3블럭
            a = k[i][j] + k[i + 1][j] + k[i + 2][j]
            answer = a if a >= answer else answer
        if j <= m - 3:  #가로 3블럭
            a = k[i][j] + k[i][j + 1] + k[i][j + 2]
            answer = a if a >= answer else answer
        if i <= n - 2 and j <= m - 2:   #ㄱ자 블럭
            b = []
            b.append(k[i][j] + k[i + 1][j] + k[i + 1][j + 1])
            b.append(k[i][j + 1] + k[i + 1][j] + k[i + 1][j + 1])
            b.append(k[i][j] + k[i][j + 1] + k[i + 1][j])
            b.append(k[i][j] + k[i][j + 1] + k[i + 1][j + 1])
            c = max(b)
            answer = c if c >= answer else answer

print(answer)