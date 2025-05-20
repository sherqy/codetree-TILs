N, K, P, T = map(int, input().split())
handshakes = sorted([tuple(map(int, input().split())) for _ in range(T)], key = lambda x: x[0])
count = [K] * N
infected = [0] * N
infected[P - 1] = 1

for t, x, y in handshakes:
    if infected[x - 1] and infected[y - 1]:
        count[x - 1] -= (1 if count[x - 1] > 0 else 0)
        count[y - 1] -= (1 if count[y - 1] > 0 else 0)
    elif infected[x - 1] == 0 and infected[y - 1] == 0:
        continue
    else:
        if infected[x - 1] and count[x - 1]:
            count[x - 1] -= 1
            infected[y - 1] = 1
        elif infected[y - 1] and count[y - 1]:
            count[y - 1] -= 1
            infected[x - 1] = 1 

print(*infected, sep = '')