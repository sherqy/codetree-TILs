a, b = map(int, input().split())
cnt = [0] * b
ans = 0

while a > 1:
    cnt[a % b] += 1
    a //= b

for i in cnt:
    ans += i * i

print(ans)