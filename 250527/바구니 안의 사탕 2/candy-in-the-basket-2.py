N, K = map(int, input().split())
pos = [0] * 101
ans = 0

for _ in range(N):
    c, p = map(int, input().split())
    pos[p] += c

for i in range(K, 102 - K):
    ans = max(sum(pos[i - K : i + K + 1]), ans)

print(ans)