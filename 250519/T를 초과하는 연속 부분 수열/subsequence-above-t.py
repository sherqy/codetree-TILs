n, t = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0
ans = 0

# Please write your code here.
for i in range(n):
    if i == 0 or arr[i] > t and arr[i - 1] > t:
        cnt += 1
    else:
        cnt = 1

    ans = max(ans, cnt)

print(ans)