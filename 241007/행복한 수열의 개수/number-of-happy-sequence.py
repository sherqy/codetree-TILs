n, m = map(int, input().split())
k = list(list(map(int, input().split()))for _ in range(n))
l = 0
p = []
answer = 0

for i in range(n):
    
    for j in range(len(k[i]) - m + 1):
        if len(set(k[i][j : j + m])) == 1:
            answer += 1
            break
    
    for o in range(n):
        p.append(k[o][i])

    
    for j in range(len(p) - m + 1):
        if len(set(p[j : j + m])) == 1:
            answer += 1
            break
    p = []

print(answer)