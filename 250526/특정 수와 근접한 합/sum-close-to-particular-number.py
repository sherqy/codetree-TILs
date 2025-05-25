import sys

N, S = map(int, input().split())
arr = list(map(int, input().split()))
diff = sys.maxsize
ans = 0

# Please write your code here.
for i in range(N - 1):
    for j in range(i + 1, N):
        if diff > abs(S - (sum(arr) - arr[i] - arr[j])):
            diff  = abs(S - (sum(arr) - arr[i] - arr[j]))

print(diff)