N = int(input())
arr = [int(input()) for _ in range(N)]
cnt = 0
ans = 0

# Please write your code here.
for i in range(N):
    if i == 0 or arr[i] * arr[i - 1] > 0:
        cnt += 1
    else:
        ans = max(ans, cnt)
        cnt = 1

print(max(ans, cnt))