n = int(input())
numbers = list(map(int, input().split()))
max_val = 0

# Please write your code here.
for i in range(n - 2):
    for j in range(i + 2, n):
        max_val = max(max_val, numbers[i] + numbers[j])

print(max_val)