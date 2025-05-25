n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
ans = 0

# Please write your code here.
for i in range(n):
    for j in range(n - 2):
        sum1 = sum(arr[i][j : j + 3])
        if j + 3 <= n - 3:
            for k in range(j + 3, n - 2):
                sum2 = sum(arr[i][k : k + 3])
                ans = max(ans, sum1 + sum2)
        else:
            for k in range(i + 1, n):
                for l in range(n - 2):
                    sum2 = sum(arr[k][l : l + 3])
                    ans = max(ans, sum1 + sum2)

print(ans)