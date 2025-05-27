n, k = map(int, input().split())
x = [''] * 10001
c = []
ans = 0
max_pos = 0

for _ in range(1, n + 1):
    pos, char = input().split()
    max_pos = max(int(pos), max_pos)
    x[int(pos)] = char

# Please write your code here.
for i in range(1, max_pos - k):
    cnt = 0

    for j in range(i, i + k + 1):
        if x[j] == 'G':
            cnt += 1
        elif x[j] == 'H':
            cnt += 2

    ans = max(cnt, ans)

print(ans)