n = int(input())
arr = [int(input()) for _ in range(n)]
cnt = 0
ans = 0

# Please write your code here.
for i in range(n):
    if i == 0 or arr[i] - arr[i - 1] > 0:
        cnt += 1
    else:
        cnt = 1
    
    ans = max(ans, cnt)

print(ans)