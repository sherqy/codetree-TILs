n = int(input())
nums = sorted(list(map(int, input().split())))
ans = 0

for i in range(n):
    ans = max(ans, nums[i] + nums[2 * n - i - 1])

print(ans)
