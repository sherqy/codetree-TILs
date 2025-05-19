N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]
c = [0] * (N + 1)

# Please write your code here.
ans = -1

for i in student:
    c[i] += 1

    if c.count(K):
        ans = c.index(K)
        break

print(ans)