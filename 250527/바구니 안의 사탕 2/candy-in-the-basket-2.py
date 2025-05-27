N, K = map(int, input().split())
pos = [0] * 101
ans = 0

for _ in range(N):
    c, p = map(int, input().split())
    pos[p] += c

for i in range(0, abs(102 - 2 * K)):
    ans = max(sum(pos[i : i + 2 * K + 1]), ans)

print(ans)