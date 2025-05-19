n = int(input())
arr = [int(input()) for _ in range(n)]
cnt = 0
ans = 0

# Please write your code here.
for i in range(n):
    if i == 0 or arr[i] == arr[i - 1]:
        cnt += 1
    else:
        ans = max(cnt, ans)
        cnt = 1

print(max(ans, cnt))