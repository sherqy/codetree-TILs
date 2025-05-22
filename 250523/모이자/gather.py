import sys

n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
min_val = sys.maxsize

for i in range(n):
    diff = 0

    for j in range(n):
        diff += abs(i - j) * A[j]

    min_val = min(min_val, diff)

print(min_val)