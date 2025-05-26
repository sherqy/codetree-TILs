n, k = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0

# Please write your code here.
for i in range(n - k + 1):
    ans = max(ans, sum(arr[i : i + k]))

print(ans)