N, M = map(int, input().split())
A = list(map(int, input().split()))
B = sorted(list(map(int, input().split())))
ans = 0

# Please write your code here.
for i in range(N - M + 1):
    if sorted(A[i : i + M]) == B:
        ans += 1

print(ans)