n, k = map(int, input().split())
x = [0] * 10001
ans = 0
max_pos = 0

for _ in range(1, n + 1):
    pos, char = input().split()
    max_pos = max(int(pos), max_pos)
    
    if char == 'G':
        x[int(pos)] = 1
    elif char == 'H':
        x[int(pos)] = 2

# Please write your code here.
for i in range(1, 10000 - k + 1):
    ans = max(sum(x[i : i + k + 1]), ans)

print(ans)