n = int(input())
arr = list(map(int, input().split()))
ans = 0

# Please write your code here.
for i in range(n):
    for j in range(i + 1, n + 1):
        if sum(arr[i : j]) / len(arr[i : j]) in arr[i : j]:
            ans += 1

print(ans)